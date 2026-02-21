from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.routing import Match, Mount
from starlette.types import ASGIApp, Receive, Scope, Send

from fastapi.routing import APIRouter


class FastAPI(Starlette):
    def __init__(
        self,
        debug: bool = False,
        routes=None,
        middleware=None,
        exception_handlers=None,
        on_startup=None,
        on_shutdown=None,
        openapi_url: str = "/openapi.json",
        redoc_url: str = "/redoc",
        docs_url: str = "/docs",
        **kwargs
    ) -> None:
        self._openapi_url = openapi_url
        self._redoc_url = redoc_url
        self._docs_url = docs_url
        super().__init__(
            debug=debug,
            routes=routes,
            middleware=middleware,
            exception_handlers=exception_handlers,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            **kwargs
        )
