from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_version: str = "0.1.0"

    # Project settings:
    project_name: str = "restfull"

    database_url: str = "sqlite:///./restfull.db"

    user_tag: str = "user"
    all_users: str = "users"
    user: str = "user"


settings = Settings()
