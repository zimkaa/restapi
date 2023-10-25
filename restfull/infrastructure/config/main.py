from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_version: str = "0.1.0"

    # Project settings:
    project_name: str = "restfull"

    database_url: str = "sqlite+aiosqlite:///./restfull.db"

    test_database_url: str = "sqlite+aiosqlite:///./test_restfull.db"

    secret: str = "1baa098e0e20a75024f773778b11ec6aff247ce1d6628f2150c86dd18768a31c"


settings = Settings()
