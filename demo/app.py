from uvicorn_requests.http.requests import Request
from uvicorn_requests.routers.router import Router
from uvicorn_requests.routers.route import Route

from .viewsets import HomePageViewSet


routes = [
    Route(r'', HomePageViewSet, name='home'),
]


async def app(scope, receive, send):

    request = Request(scope, receive)

    assert request.type == 'http'

    response = Router(
        routes=routes
    ).get_reponse(request)

    await send(response.start)
    await send(response.body)
