FROM python:3.11.9

WORKDIR /channelbot

COPY . /channelbot/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install


CMD ["poetry", "run", "uvicorn", "channelbot.bot:app", "--host", "0.0.0.0", "--port", "8000", "--log-config=log_config.ini", "--log-level=debug", "--reload", "--reload-dir", "."]

EXPOSE 8000
