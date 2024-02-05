from zoneinfo import ZoneInfo

from pydantic import Field, PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from core.paths import setup_path


class Settings(BaseSettings):
    debug: bool = Field(default=False)

    timezone_region: str = Field(default="Asia/Yekaterinburg")

    db_name: str = Field(default="project")
    db_user: str = Field(default="postgres")
    db_password: str = Field(default="postgres")
    db_server: str = Field(default="localhost:5432")

    model_config = SettingsConfigDict(env_file=setup_path(".env", root=True), env_file_encoding="utf-8")

    @computed_field  # type: ignore[misc]
    @property
    def db_uri(self) -> str:
        postgres_uri = f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_server}/{self.db_name}"
        return str(PostgresDsn(postgres_uri))

    @computed_field  # type: ignore[misc]
    @property
    def timezone(self) -> ZoneInfo:
        return ZoneInfo(self.timezone_region)


settings = Settings()
