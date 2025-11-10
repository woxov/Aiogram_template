from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types import Message

from Bot.Repositories.Admin import AdminRepository


class AdminService:
    @staticmethod
    async def get_all_users_quontity(
        session: AsyncSession, message: Message
    ) -> Message:
        users = await AdminRepository.get_all_users(session)
        return await message.answer(text=f"Users: {len(users)}")
