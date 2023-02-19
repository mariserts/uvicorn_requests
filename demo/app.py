from uvicorn_requests.http.requests import Request
from uvicorn_requests.routers.router import Router
from uvicorn_requests.routers.route import Route

from .viewsets import HomePageViewSet


ROUTES = [
    Route(r'', HomePageViewSet, name='home'),
]


TEMPLATE_PATHS = [
    'demo/templates/'
]


async def app(scope, receive, send):

    request = Request(
        scope,
        receive,
        encoding='utf-8',
        template_paths=TEMPLATE_PATHS,
    )

    assert request.type == 'http'

    response = Router(ROUTES).get_response(request)

    await send(response.start)
    await send(response.body)
