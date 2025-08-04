from typing import Dict, List, Optional
from datetime import datetime
from ...domain.entities.user import User
from ...core.security import get_password_hash

class MockDatabase:
    def __init__(self):
        self._users: Dict[int, User] = {}
        self._user_counter = 1
        
        self._create_default_user()
    
    def _create_default_user(self):
        admin_user = User(
            id=self._user_counter,
            username="admin",
            email="admin@example.com",
            hashed_password=get_password_hash("admin123"),
            is_active=True,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self._users[self._user_counter] = admin_user
        self._user_counter += 1
    
    async def create_user(self, user: User) -> User:
        user.id = self._user_counter
        user.created_at = datetime.now()
        user.updated_at = datetime.now()
        self._users[self._user_counter] = user
        self._user_counter += 1
        return user
    
    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)
    
    async def get_user_by_username(self, username: str) -> Optional[User]:
        for user in self._users.values():
            if user.username == username:
                return user
        return None
    
    async def get_user_by_email(self, email: str) -> Optional[User]:
        for user in self._users.values():
            if user.email == email:
                return user
        return None
    
    async def get_all_users(self) -> List[User]:
        return list(self._users.values())
    
    async def update_user(self, user: User) -> User:
        if user.id and user.id in self._users:
            user.updated_at = datetime.now()
            self._users[user.id] = user
            return user
        raise ValueError(f"User with ID {user.id} not found")
    
    async def delete_user(self, user_id: int) -> bool:
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False

mock_db = MockDatabase()