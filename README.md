# CyberHelper

Учебный Telegram-бот на Python с инструментами для изучения основ кибербезопасности.

## Возможности

- `/start` — запуск бота
- `/hash <text>` — SHA-256 хеширование
- `/encode <text>` — кодирование Base64
- `/decode <base64>` — декодирование Base64
- `/whois <domain>` — получение WHOIS-информации
- `/dns <domain>` — получение A-записей DNS
- `/headers <url>` — получение HTTP-заголовков
- `/port <host> <port>` — проверка TCP-порта
- `/help` — список команд

## Структура проекта

```text
CyberHelper/
├── bot.py
├── handlers.py
├── tools.py
├── requirements.txt
└── .gitignore