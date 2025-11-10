import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from sqlalchemy.ext.asyncio import AsyncSession

from Bot.Services.User.service import UserService


class UserHandler:
    def __init__(self, router: Router) -> None:
        self.router = router
        self._register_handlers()
        self.logger = logging.getLogger(__name__)

    def _register_handlers(self) -> None:
        self.router.message(Command("start"))(self.start_cmd)
        self.router.message(Command("help"))(self.help_cmd)
        self.router.message(F.text)(self.echo_message)

    async def start_cmd(self, message: Message, session: AsyncSession) -> None:
        await UserService.start_user(session=session, message=message)

    async def help_cmd(self, message: Message) -> None:
        await message.answer(text="This is /help command")

    async def echo_message(self, message: Message) -> None:
        await message.answer(
            text=f"User ID: {message.from_user.id}\nSend message: {message.text}"
        )
