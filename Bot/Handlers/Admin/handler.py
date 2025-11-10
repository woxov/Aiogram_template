from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from Bot.Middleware import AdminMiddleware
from Bot.Services.Admin.service import AdminService


class AdminHandler:
    def __init__(self, router: Router) -> None:
        self.router = router
        self._register_handlers()
        self.router.message.middleware(AdminMiddleware())

    def _register_handlers(self) -> None:
        self.router.message(Command("admin"))(self.admin_cmd)
        self.router.message(Command("users"))(self.users_cmd)

    async def admin_cmd(self, message: Message) -> None:
        await message.answer(text="Admin panel")

    async def users_cmd(self, message: Message, session: AsyncSession) -> None:
        await AdminService.get_all_users_quontity(session=session, message=message)
