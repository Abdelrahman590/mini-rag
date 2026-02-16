from fastapi import APIRouter,FastAPI 
import os
router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)


@router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
            app_name:"Welcome to ALL!"
            ,app_version:app_version
            
            }