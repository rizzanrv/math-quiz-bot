import disnake
from disnake.ext import commands
import asyncio

from src.config import Config


def main():
    intents = disnake.Intents.default()
    intents.message_content = True

    bot = commands.Bot(
        command_prefix=Config.PREFIX,
        intents=intents,
        test_guilds=[123456789012345678],  # укажите свой сервер для быстрой синхронизации слеш-команд
    )

    @bot.event
    async def on_ready():
        print(f"Зашёл как {bot.user} • {bot.user.id}")
        print(f"Серверов: {len(bot.guilds)}")

    bot.load_extension("src.cogs.quiz")

    bot.run(Config.TOKEN)


if __name__ == "__main__":
    main()