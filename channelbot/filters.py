from aiogram import Bot, types
from aiogram.filters.base import Filter
from aiogram.enums.chat_type import ChatType

from typing import List

from channelbot.settings import GROUP_ID


class ChatFilter(Filter):
    def __init__(self, chat_ids: List[int] = [], chat_types: List[ChatType] = []) -> None:
        self.chat_ids = chat_ids
        self.chat_types = chat_types

    async def __call__(self, msg: types.Message) -> bool:
        return msg.chat.type in self.chat_types if len(self.chat_types) > 1 else True \
            and msg.chat.id in self.chat_ids if len(self.chat_ids) > 0 else True


class AdminFilter(Filter):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def __call__(self, msg: types.Message) -> bool:
        admins: list = await self.bot.get_chat_administrators(chat_id=GROUP_ID)
        return msg.from_user is not None and msg.from_user.id in admins
