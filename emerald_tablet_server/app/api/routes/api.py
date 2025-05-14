from fastapi import APIRouter

from emerald_tablet_server.app.api.routes import message_crud

router = APIRouter()
router.include_router(message_crud.router, tags=["repository"], prefix="/v1/message")
