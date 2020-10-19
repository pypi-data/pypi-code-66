"""HTTP routes for the demo REST API."""
from fastapi import APIRouter, Response
from loguru import logger

router = APIRouter()


@router.on_event("startup")
def on_startup() -> None:
    """"This function is called once after application initialization.

    If any error is raised in this function, the application will never start.
    """
    logger.info("Starting router!")


@router.on_event("shutdown")
def on_shutdown() -> None:
    """This function is called once before application is stopped.

    If any error is raised in this function, application will exit immediately.
    """
    logger.info("Stopping router!")


@router.get(
    "/", summary="Get an empty response.", status_code=202, tags=["Demonstration"],
)
def demo_response() -> Response:
    """Return an empty response when successful. This route does not accept any parameter."""
    return Response(status_code=202)
