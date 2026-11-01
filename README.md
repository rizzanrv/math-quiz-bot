# math-quiz-bot

Discord-бот с викториной по математике: 15 случайных задач, по 45 секунд на
ответ, алгебра и геометрия. disnake.

Проект писался в 2023–2024 для «Больших вызовов» (Сириус), в 2026 переписан на
актуальную версию библиотеки и модульную структуру.

## Запуск

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

# .env в корне
DISCORD_TOKEN=ваш_токен

python src/bot.py
```

## Что умеет

- `/start-quiz` — сессия из 15 случайных задач
- два раздела: `src/data/algebra.py`, `src/data/geometry.py`
- таймер на вопрос (45 с), разбор после каждого ответа
- итоговый эмбед с результатом

## Структура

```
src/bot.py           запуск
src/config.py        загрузка .env
src/cogs/quiz.py     логика викторины
src/data/            банк вопросов
```

## Ограничения

- Вопросы лежат статикой в `src/data/`, генератора нет.
- Тестов нет.
- Один язык — русский.

## Лицензия

MIT, см. [LICENSE](LICENSE).
