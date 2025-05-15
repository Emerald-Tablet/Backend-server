from fastapi import APIRouter, HTTPException, Body
from data import BasicResponse
from data.message import Message
from typing import Annotated

router = APIRouter()

@router.post(
    "/create",
    response_model=BasicResponse,
    status_code=200,
    name="create:message"
)
async def create_message(message:Annotated[Message,Body()]):
    if not message:
            raise HTTPException(status_code=404, detail="'message' argument invalid!")
    try:
        pass
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return BasicResponse(success=True,message="message create success")


@router.update(
    "/update",
    response_model=BasicResponse,
    status_code=200,
    name="update:message"
)
async def update_message(message:Annotated[Message,Body()]):
    if not message:
            raise HTTPException(status_code=404, detail="'message' argument invalid!")
    try:
        pass
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return BasicResponse(success=True,message="message update success")

@router.delete(
    "/delete",
    response_model=BasicResponse,
    status_code=200,
    name="delete:message"
)
async def delete_message(message_id:Annotated[str,Body()]):
    if not message_id:
            raise HTTPException(status_code=404, detail="'message' argument invalid!")
    try:
        pass
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return BasicResponse(success=True,message=f"{message_id} delete success")
