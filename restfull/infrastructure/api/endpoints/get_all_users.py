from fastapi import APIRouter, Response


router = APIRouter()


@router.get("", summary="Get all users")
async def get_users() -> Response:
    return Response(
        content="SUCCESS",
        status_code=200,
        media_type="text/plain",
    )
