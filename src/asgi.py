import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.urls import add_routes

logging.basicConfig(
    filename='mailer.log',
    filemode='a',
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,
)


def create_app() -> FastAPI:
    app = FastAPI(
        title='Asadal pay',
        debug=True,
        openapi_url='/api/openapi.json',
        docs_url='/api/docs',
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=tuple(
            {
                '*',
            },
        ),
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    add_routes(app)

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        'asgi:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
    )
