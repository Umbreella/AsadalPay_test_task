from fastapi import FastAPI, status

from src.api.mail import send_email


def add_routes(app: FastAPI) -> None:
    app.add_api_route(
        path='/api/send_email',
        endpoint=send_email,
        methods=['POST'],
        status_code=status.HTTP_201_CREATED,
    )
