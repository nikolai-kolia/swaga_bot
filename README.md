# Swagushka ICEGERGERT Bot

Telegram-бот для флуда и настроения.
Отвечает в личных сообщениях на команду /swaga случайной строчкой из песен ICEGERGERT.

Проект сделан в рамках тестового задания для Информационного комитета.

---

Возможности

- /start — приветственное сообщение
- /swaga — присылает случайную строчку из песен ICEGERGERT
- /vibe — присылает случайную мотивационную фразу

---

Структура проекта

.
├── main.py        - Основной файл бота
├── lyrics.py      - Файл со строчками песен
├── requirements.txt
└── README.md

---

Установка и запуск

1. Склонировать репозиторий

git clone https://github.com/USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME

---

2. Создать и активировать виртуальное окружение (рекомендуется)

python -m venv venv

Windows (PowerShell):
venv\Scripts\activate

Linux / macOS:
source venv/bin/activate

---

3. Установить зависимости

pip install -r requirements.txt

---

4. Запустить бота

В терминале написать: python main.py

Если всё успешно, появится сообщение:

Start polling
Run polling for bot ...

Это значит, что бот работает.

---

Как пользоваться

Найди бота в Telegram и напиши:

/start
/swaga
/vibe

---

Используемые технологии

- Python 3.10+
- aiogram 3
- Telegram Bot API

---

Примечание

Если бот не отвечает:

- проверь, что он запущен
- проверь, что токен вставлен правильно
- проверь, что ты пишешь ему в личные сообщения
