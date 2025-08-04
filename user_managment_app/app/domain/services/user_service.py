from typing import List, Optional
from datetime  import datetime
from ..entities.user import User
from ..repositories.user_repository import UserRepository
from ...core.security import get_password_hash
from ...core.exceptions import UserAlreadyExistsException, UserNotFoundException


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, username: str, email:str, password: str) -> User:
        existing_user = await self.user_repository.get_by_username(username)
        existing_email = await self.user_repository.get_by_email(email)

        if existing_user or existing_email:
            raise UserAlreadyExistsException(f"User with username '{username}' already existis")   
        
        hashed_password = get_password_hash(password)
        user = User(
            id=None,
            username=username,
            email = email,
            hashed_password=hashed_password,
            is_active=True,
            created_at = datetime.now(),
            updated_at = datetime.now()
        )

        return await self.user_repository.create(user)
    
    
    async def get_user_by_id(self, user_id: int)->User:
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found")
        return user
    
    async def get_all_users(self) -> List[User]:
        return await self.user_repository.get_all()

    async def update_user(self, user_id: int, username: str = None, email: str = None) -> User:
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found")
        
        if username:
            user.username = username
        if email:
            user.email = email

        user.updated_at = datetime.now()

        return await self.user_repository.update(user)
    

    async def delete_user(self, user_id) -> bool:
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(f"User with ID {user_id} not found")
        
        return await self.user_repository.delete(user_id)



        