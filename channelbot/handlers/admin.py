from aiogram import Router, types
from aiogram.filters.command import Command

from channelbot.settings import _


router = Router()


@router.message(Command('start'))
async def start(msg: types.Message):
    await msg.reply(_('Hello! Here you can anonymously communicate with your followers. Just choose one below to start chatting. If this list is empty, nobody is texting you'))
