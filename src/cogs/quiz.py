import random
import disnake
from disnake.ext import commands

from src.data.algebra import ALGEBRA_QUESTIONS
from src.data.geometry import GEOMETRY_QUESTIONS


class QuizCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="start-quiz", description="Начать математическую викторину")
    async def start_quiz(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        tasks = [self._algebra_task, self._geometry_task]
        total_correct = 0
        total_tasks = 15

        for i in range(1, total_tasks + 1):
            task_func = random.choice(tasks)
            correct = await task_func(inter, i)
            total_correct += correct

        embed = disnake.Embed(
            title="Викторина завершена!",
            description=f"Вы правильно ответили на **{total_correct}** из **{total_tasks}** задач.",
            color=disnake.Color.green() if total_correct >= 10 else disnake.Color.orange()
        )
        await inter.edit_original_message(embed=embed)

    async def _algebra_task(self, inter: disnake.ApplicationCommandInteraction, number: int) -> int:
        return await self._ask_question(inter, number, ALGEBRA_QUESTIONS, "Алгебра")

    async def _geometry_task(self, inter: disnake.ApplicationCommandInteraction, number: int) -> int:
        return await self._ask_question(inter, number, GEOMETRY_QUESTIONS, "Геометрия")

    async def _ask_question(
        self,
        inter: disnake.ApplicationCommandInteraction,
        number: int,
        question_pool: list[dict],
        category: str
    ) -> int:
        q = random.choice(question_pool)
        correct = q["correct"]

        embed = disnake.Embed(
            title=f"Задача {number} • {category}",
            description=q["question"],
            color=disnake.Color.blue()
        )
        embed.add_field(name="Варианты ответа", value="\n".join(f"{i+1}) {opt}" for i, opt in enumerate(q["options"])), inline=False)

        await inter.edit_original_message(embed=embed, content=None)

        def check(m: disnake.Message):
            return m.author == inter.author and m.channel == inter.channel

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=45.0)
            answer = msg.content.strip()

            if answer == correct:
                await inter.channel.send(embed=disnake.Embed(
                    description="✅ **Правильно!**",
                    color=disnake.Color.green()
                ))
                return 1
            else:
                await inter.channel.send(embed=disnake.Embed(
                    description=f"❌ Неправильно. Правильный ответ: **{correct}**",
                    color=disnake.Color.red()
                ))
                return 0

        except disnake.errors.HTTPException:
            pass  # бот мог быть выключен
        except TimeoutError:
            await inter.channel.send(embed=disnake.Embed(
                description="⏰ Время вышло!",
                color=disnake.Color.dark_grey()
            ))
            return 0


def setup(bot: commands.Bot):
    bot.add_cog(QuizCog(bot))