from datetime import timedelta 
from ..repositories.user_repository import UserRepository
from ...core.security import verify_password, create_access_token
from ...core.config import settings
from ...core.exceptions import InvalidCredentialsException


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def authenticate_user(self, username:str, password: str) ->str:
        user = await self.user_repository.get_by_username(username)

        if not user or not verify_password(password, user.hashed_password):
            raise InvalidCredentialsException("Invalid username or password")
        
        if not user.is_active:
            raise InvalidCredentialsException("User account is inactive")
        
        access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
        return create_access_token(data={'sub':user.username}, expires_delta=access_token_expires)
        
        