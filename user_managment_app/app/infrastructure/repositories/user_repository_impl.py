from typing import List, Optional
from ...domain.entities.user import User
from ...domain.repositories.user_repository import UserRepository

class UserRepositoryImpl(UserRepository):
    def __init__(self, db):
        self.db = db
    
    async def create(self, user: User) -> User:
        return await self.db.create_user(user)
    
    async def get_by_id(self, user_id: int) -> Optional[User]:
        return await self.db.get_user_by_id(user_id)
    
    async def get_by_username(self, username: str) -> Optional[User]:
        return await self.db.get_user_by_username(username)
    
    async def get_by_email(self, email: str) -> Optional[User]:
        return await self.db.get_user_by_email(email)
    
    async def get_all(self) -> List[User]:
        return await self.db.get_all_users()
    
    async def update(self, user: User) -> User:
        return await self.db.update_user(user)
    
    async def delete(self, user_id: int) -> bool:
        return await self.db.delete_user(user_id)