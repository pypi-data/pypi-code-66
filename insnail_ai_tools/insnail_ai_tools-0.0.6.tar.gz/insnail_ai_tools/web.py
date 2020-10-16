from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def create_fast_api_app(cors: bool = True, **kwargs):
    app = FastAPI(**kwargs)
    if cors:
        # 跨域
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        return app
    return app
