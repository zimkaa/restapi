from sqlalchemy.ext.asyncio import create_async_engine

from restfull.infrastructure.config import settings


engine = create_async_engine(
    settings.database_url,
    echo=False,
)
