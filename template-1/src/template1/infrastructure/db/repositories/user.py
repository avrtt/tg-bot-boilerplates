from typing import Optional

from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from template1.infrastructure.db import models

from template1.application.common.repositories import UserRepository

from template1.domain.entities.user import User
from template1.domain.value_objects.user import UserId


class UserRepositoryImpl(UserRepository):
    """Database abstraction layer"""

    # if you implement some reading logic there
    # you can use converters for converting ORM objects to domain entities
    # your repository methods must return domain entities, not ORM objects.
    # I cant show it there, because this demo user model has not additional fields like age, name
    # and here is not read logic

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User) -> User:
        db_user = models.User(
            user_id=user.user_id.to_raw(),
        )

        self.session.add(db_user)

        return user

    async def exists(self, user_id: UserId) -> bool:
        q = select(exists().where(models.User.user_id == user_id.to_raw()))

        res = await self.session.execute(q)

        is_exists: Optional[bool] = res.scalar()

        if not is_exists:
            is_exists = False

        return is_exists
