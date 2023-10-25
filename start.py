from loguru import logger

from restfull.infrastructure.api.application import app


if __name__ == "__main__":
    import uvicorn

    logger.add(
        "API_logs.log",
        format="{time} {level} {message}",
        level="TRACE",
        rotation="10 MB",
        compression="zip",
    )

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )
