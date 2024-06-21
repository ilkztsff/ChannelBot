from aiogram import types
from aiogram.filters.base import Filter
from aiogram.enums.chat_type import ChatType
from aiogram.methods.get_chat_administrators import GetChatAdministrators

from typing import List

from channelbot.settings import GROUP_ID


class ChatFilter(Filter):
    def __init__(self, chat_ids: List[int] = [], chat_types: List[ChatType] = []) -> None:
        self.chat_ids = chat_ids
        self.chat_types = chat_types

    async def __call__(self, msg: types.Message) -> bool:
        return msg.chat.type in self.chat_types if len(self.chat_types) > 1 else True \
            and msg.chat.id in self.chat_ids if len(self.chat_ids) > 0 else True
