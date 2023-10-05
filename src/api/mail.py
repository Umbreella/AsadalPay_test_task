import logging

from fastapi_mail import MessageSchema, MessageType
from fastapi_mail.errors import ConnectionErrors
from starlette.background import BackgroundTasks

from src.schema.email import EmailCreateSchema
from src.schema.response import DetailSchema
from src.smtp import smtp_server


async def _try_send_email(message: MessageSchema) -> None:
    try:
        await smtp_server.send_message(message)
    except ConnectionErrors as ex:
        logging.info(ex.expression)
    else:
        logging.info(f'Email sent: {message.subject} ({message.recipients})')


async def send_email(
    data: EmailCreateSchema,
    background_tasks: BackgroundTasks,
) -> DetailSchema:
    message: MessageSchema = MessageSchema(
        recipients=[data.to],
        subject=data.subject,
        body=data.message,
        subtype=MessageType.plain,
    )

    background_tasks.add_task(_try_send_email, message)

    return DetailSchema(
        detail='Email sent.',
    )
