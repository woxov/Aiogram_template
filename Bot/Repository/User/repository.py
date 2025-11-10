from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from Bot.Database.model import User


class UserRespository:
    @staticmethod
    async def add_user(
        session: AsyncSession,
        telegram_id: int,
        first_name: str,
        username: str | None,
    ) -> User:
        new_user = User(
            Telegram_id=telegram_id, First_name=first_name, Username=username
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user

    @staticmethod
    async def get_user_by_telegram_id(
        session: AsyncSession,
        telegram_id: int,
    ) -> User | None:
        return await session.scalar(select(User).where(User.Telegram_id == telegram_id))
