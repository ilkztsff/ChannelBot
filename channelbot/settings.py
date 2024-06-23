from dotenv import load_dotenv

from os import environ
import gettext


load_dotenv()

TOKEN: str = environ['BOT_TOKEN']

HOST: str = environ['HOST']
WEBHOOK_PATH: str = f'bot/{TOKEN}'
WEB_SERVER_URL: str = environ['WEB_SERVER_URL']
WEBHOOK_URL: str = f'{WEB_SERVER_URL}{"/" if not WEB_SERVER_URL.endswith("/") else ""}{WEBHOOK_PATH}'

REDIS_PORT = int(environ['REDIS_PORT'])
REDIS_PASSWORD: str = environ['REDIS_PASSWORD']

CHANNEL_ID = int(environ['CHANNEL_ID'])
GROUP_ID = int(environ['GROUP_ID'])

TIMEOUT = int(environ.get('TIMEOUT', 0))
LANGUAGE: str = environ.get('LANGUAGE', 'en')


translation = gettext.translation('messages', localedir='./locales', languages=[LANGUAGE])
translation.install()
_ = translation.gettext
