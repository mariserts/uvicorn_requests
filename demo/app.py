from uvicorn_requests.requests import Request
from uvicorn_requests.responses import Response


async def app(scope, receive, send):

    request = Request(scope, receive)

    assert request.type == 'http'

    response = Response(
        request,
        'Hello, world!',
        status=200,
        headers = {
            'content-type': 'text/plain'
        }
    )

    await send(response.start)
    await send(response.body)
