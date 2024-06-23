<p align="center">
    <a href="https://github.com/ilkztsff/ChannelBot/blob/dev/LICENSE">
        <img alt="license" src="https://img.shields.io/github/license/ilkztsff/ChannelBot?label=License&color=yellow&style=for-the-badge">
    </a>
    <img alt="python" src="https://img.shields.io/badge/3.11.9-yellow?color=yellow&label=Python&style=for-the-badge">
    <a href="https://github.com/ilkztsff/ChannelBot/actions/workflows/check.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/ilkztsff/ChannelBot/check.yml?branch=dev&style=for-the-badge&label=linter&color=yellow">
    </a>
</p>

<h1 align="center">ChannelBot</h1>


## ✍ About

A simple bot for managing your telegram channel and anonymous communicating with your followers


## 🛠 Build commands

Required to have `git`, `make`, `docker` и `docker-compose` installed

Download project from GitHub
```bash
git clone https://github.com/ilkztsff/ChannelBot/
```
<br>

Build docker container
```bash
make build
```
<br>

Update dependencies
```bash
make update
```
<br>

Run this project
```bash
make start
```
<br>

Run the project in a background mode
```bash
make up
```
<br>

Stop containers
```bash
make stop
```
<br>

Remove stopped containers and data
```bash
make rm
```
<br>

Lint the project
```bash
make lint
```
<br>


## 🖥 Enviromental variables

All required enviromental variables are below. Examples [here](https://github.com/ilkztsff/ChannelBot/blob/dev/.env.example)

- `HOST` - server host

- `WEB_SERVER_URL` - url of a web server for getting updates from telegram

- `BOT_TOKEN` - your telegram bot token, you can get it from [@BotFather](https://t.me/BotFather)

- `LANGUAGE` - language for your telegram bot, now only english(`en`) and russian(`ru`) are available

- `TIMEOUT` - flood interval

- `CHANNEL_ID` - id of your telegram channel(without `-100` prefix)

- `GROUP_ID` - id of your telegram group for commen(without `-100` prefix)

- `REDIS_PORT` - port for redis database

- `REDIS_PASSWORD` - password for redis databas


## 💿 [Dependencies](https://github.com/ilkztsff/ChannelBot/blob/dev/pyproject.toml)

- **[aiogram](https://pypi.org/project/aiogram) - 3.6.0**

- **[fastapi](https://pypi.org/project/fastapi) - 0.111.0**

- **[uvicorn](https://pypi.org/project/uvicorn) - 0.29.0**

- **[python-dotenv](https://pypi.org/project/python-dotenv) - 1.0.1**

- **[redis](https://pypi.org/project/redis) - 5.0.4**

- **[flake8](https://pypi.org/project/flake8) - 7.0.0**

- **[mypy](https://pypi.org/project/mypy) - 1.10.0**
