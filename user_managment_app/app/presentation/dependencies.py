from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..domain.services.user_service import UserService
from ..domain.services.auth_serivice import AuthService
from ..infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from ..infrastructure.database.mock_db import mock_db
from ..core.security import verify_token
from ..domain.entities.user import User

# Security
security = HTTPBearer()

# Repository
def get_user_repository() -> UserRepositoryImpl:
    return UserRepositoryImpl(mock_db)

# Services
def get_user_service(
    user_repo: UserRepositoryImpl = Depends(get_user_repository)
) -> UserService:
    return UserService(user_repo)

def get_auth_service(
    user_repo: UserRepositoryImpl = Depends(get_user_repository)
) -> AuthService:
    return AuthService(user_repo)

# Authentication dependency
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_service: UserService = Depends(get_user_service)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    username = verify_token(credentials.credentials)
    if username is None:
        raise credentials_exception
    
    try:
        user = await user_service.user_repository.get_by_username(username)
        if user is None:
            raise credentials_exception
        return user
    except Exception:
        raise credentials_exception