from dataclasses import dataclass
from datetime import date, datetime

from users.domain.user.roles import UserRole
from users.domain.user.user_id import UserId
from users.domain.user.value_objects import Contacts, Fullname


@dataclass(frozen=True)
class UserReadModel:
    user_id: UserId
    fullname: Fullname
    contacts: Contacts
    user_role: UserRole
    birth_date: date | None
    created_at: datetime
