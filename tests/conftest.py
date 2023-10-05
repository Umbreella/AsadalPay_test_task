from contextlib import ExitStack

import pytest
from httpx import AsyncClient

from src.asgi import create_app
from src.smtp import smtp_server

smtp_server.config.SUPPRESS_SEND = 1


@pytest.fixture(autouse=True)
def app():
    with ExitStack():
        yield create_app()


@pytest.fixture
async def client(app):
    async with AsyncClient(app=app, base_url='http://testserver') as c:
        yield c
