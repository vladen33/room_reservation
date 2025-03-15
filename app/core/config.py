from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    description: str = 'Описание проекта по бронированию переговорок'

    class Config:
        extra = 'ignore'
        env_file = '.env'

settings = Settings()
