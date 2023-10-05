from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DEBUG: bool = False
    MAIL_USERNAME: str = ''
    MAIL_PASSWORD: str = ''
    MAIL_PORT: int = 25
    MAIL_SERVER: str = 'localhost'
    MAIL_TLS: bool = False
    MAIL_SSL: bool = False
    MAIL_FROM: EmailStr

    class Config:
        env_prefix = 'APP_APPLICATION_'


config = Config()
