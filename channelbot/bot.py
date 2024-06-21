from aiogram import Bot, Dispatcher, types
from aiogram.enums.chat_type import ChatType

from fastapi import FastAPI, APIRouter
from redis import Redis

from contextlib import asynccontextmanager

from channelbot.filters import ChatFilter, AdminFilter
from channelbot.handlers import admin_rt, channel_rt, group_rt, private_rt
from channelbot.settings import WEBHOOK_URL, WEBHOOK_PATH, TOKEN, GROUP_ID, CHANNEL_ID, \
    HOST, REDIS_PORT, REDIS_PASSWORD


@asynccontextmanager
async def lifespan(app: FastAPI):
    private_rt.message.filter(ChatFilter(chat_types=[ChatType.PRIVATE]))
    admin_rt.message.filter(AdminFilter(bot=bot), ChatFilter(chat_types=[ChatType.PRIVATE]))
    group_rt.message.filter(ChatFilter([GROUP_ID], [ChatType.GROUP, ChatType.SUPERGROUP]))
    channel_rt.channel_post.filter(ChatFilter([CHANNEL_ID], [ChatType.CHANNEL]))

    dp.include_routers(admin_rt, channel_rt, group_rt, private_rt)
    await bot.set_webhook(WEBHOOK_URL)

    yield


redis = Redis(host=HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)
app = APIRouter(lifespan=lifespan)

bot = Bot(TOKEN)
dp = Dispatcher()


@app.post(f'/{WEBHOOK_PATH}')
async def telegram_webhook(request: dict):
    update = types.Update(**request)
    await dp.feed_update(bot, update)
