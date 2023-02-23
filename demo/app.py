from typing import Type

from uvicorn_requests.routers.route import Route
from uvicorn_requests.app import app as uvicorn_requests_app

from .viewsets import (
    HomePageViewSet,
    JSONDetailViewSet,
    JSONRootViewSet,
    PageViewSet,
)


ROUTES = [
    Route(r'/', HomePageViewSet, name='home'),
    Route(r'/page/', PageViewSet, name='page'),
    Route(r'/api/', JSONRootViewSet, name='api'),
    Route(r'/api/(?P<pk>\d+)/', JSONDetailViewSet, name='api-value'),
]


TEMPLATE_PATHS = [
    'demo/templates/'
]


# #
# # 95% 84ms Med: 64
# #

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

# #
# # 95% 63ms Med: 44
# #

# async def read_body(receive):
#     """
#     Read and return the entire body from an incoming ASGI message.
#     """
#     body = b''
#     more_body = True
#
#     while more_body:
#         message = await receive()
#         body += message.get('body', b'')
#         more_body = message.get('more_body', False)
#
#     return body
#
#
# async def app(scope, receive, send):
#     """
#     Echo the request body back in an HTTP response.
#     """
#     body = await read_body(receive)
#     await send({
#         'type': 'http.response.start',
#         'status': 200,
#         'headers': [
#             [b'content-type', b'text/plain'],
#         ]
#     })
#     await send({
#         'type': 'http.response.body',
#         'body': str.encode(f'<h1>Hello world</h1>{scope}'),
#     })
