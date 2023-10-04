import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


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

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        'asgi:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
    )
