from fastapi import FastAPI
from app.presentation.routers import auth, users
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="A clean architecture FastAPI application with user management and authentication",
    version="1.0.0"
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to User Management API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)