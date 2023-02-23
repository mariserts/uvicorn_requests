from typing import Type

from uvicorn_requests.routers.route import Route
from uvicorn_requests.app import app as uvicorn_requests_app

from .viewsets import HomePageViewSet, JSONDetailViewSet, JSONRootViewSet


ROUTES = [
    Route(r'', HomePageViewSet, name='home'),
    Route(r'/api/', JSONRootViewSet, name='api'),
    Route(r'/api/(?P<pk>\d+)/', JSONDetailViewSet, name='api-value'),
]


TEMPLATE_PATHS = [
    'demo/templates/'
]


async def app(
    scope: dict,
    receive: bytes,
    send: Type
) -> None:

    await uvicorn_requests_app(
        scope,
        receive,
        send,
        routes=ROUTES,
        template_paths=TEMPLATE_PATHS
    )
