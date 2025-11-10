from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from Bot.Database.model import User


class AdminRepository:
    @staticmethod
    async def get_all_users(session: AsyncSession) -> List[User]:
        result = await session.scalars(select(User))
        return list(result.all())
