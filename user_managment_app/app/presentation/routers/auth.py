from fastapi import APIRouter, Depends, HTTPException, status
from ..schemas.auth_schemas import Token, UserLogin
from ..schemas.user_schemas import UserCreate, UserResponse
from ..dependencies import get_auth_service, get_user_service
from ...domain.services.user_service import UserService
from ...domain.services.auth_serivice import AuthService
from ...core.exceptions import InvalidCredentialsException, UserAlreadyExistsException

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    try:
        user = await user_service.create_user(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password
        )
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    except UserAlreadyExistsException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/login", response_model=Token)
async def login(
    user_credentials: UserLogin,
    auth_service: AuthService = Depends(get_auth_service)
):
    try:
        access_token = await auth_service.authenticate_user(
            username=user_credentials.username,
            password=user_credentials.password
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except InvalidCredentialsException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )