# PrinterBot

## Требования
Убедитесь, что у вас установлены следующие компоненты:
-  **Docker** — для контейнеризации приложения;
-  **Docker Compose** — для управления многоконтейнерными приложениями;

## Установка и настройка
1. Клонируйте репозиторий:
```shell
git clone https://github.com/Dilemma25/printer-bot.git
cd printer-bot
```

2. Создайте .env и заполните его:
```shell
make create-env
```

```dotenv
# Токен вашего Telegram-бота
BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11

# Ваш Telegram ID (куда бот будет пересылать фотографии для печати)
ADMIN_ID=123456789
```
Замените `BOT_TOKEN` на токен, полученный у [@BotFather](https://t.me/BotFather),  
`ADMIN_ID` на свой Telegram ID.

# Работа с приложением
## команды
- `make up` - Собрать и запустить контейнеры;
- `make down` - Разобрать контейнеры;
- `make start` - Запустить контейнеры;
- `make stop` - Остановить контейнеры;
- `make show-logs` - Показать логи контейнеров;
- `make follow-logs` - Показать логи контейнеров в режиме **follow**;
