from fastapi_mail import ConnectionConfig, FastMail

from src.config import config

smtp_server = FastMail(
    ConnectionConfig(
        MAIL_USERNAME=config.MAIL_USERNAME,
        MAIL_PASSWORD=config.MAIL_PASSWORD,
        MAIL_SERVER=config.MAIL_SERVER,
        MAIL_PORT=config.MAIL_PORT,
        MAIL_STARTTLS=config.MAIL_TLS,
        MAIL_SSL_TLS=config.MAIL_SSL,
        MAIL_FROM=config.MAIL_FROM,
    ),
)
