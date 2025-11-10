from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from Bot.Repositories.User.repository import UserRespository


class UserService:
    @staticmethod
    async def start_user(session: AsyncSession, message: Message) -> Message:
        if not message.from_user:
            raise ValueError("message.from_user is None")

        telegram_id = message.from_user.id
        first_name = message.from_user.first_name
        username = message.from_user.username

        check = await UserRespository.get_user_by_telegram_id(
            session=session,
            telegram_id=telegram_id,
        )

        if not check:
            await UserRespository.add_user(
                session=session,
                telegram_id=telegram_id,
                first_name=first_name,
                username=username,
            )

        return await message.answer(text="Hello world!!!")
