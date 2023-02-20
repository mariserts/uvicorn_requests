# -*- coding: utf-8 -*-
from typing import List, Type

from .conf import settings
from .http.requests import Request
from .routers.router import Router


async def read_body(
    receive: bytes
) -> bytes:

    body = b''
    more_body = True

    while more_body:
        message = await receive()
        body += message.get('body', b'')
        more_body = message.get('more_body', False)

    return body


async def app(
    scope: dict,
    receive: bytes,
    send: Type,
    router_class: Type = Router,
    routes: List[Type] = [],
    template_paths: List[str] = [],
) -> None:

    assert scope['type'] == 'http'

    body = await read_body(receive)

    request = Request(
        scope,
        body,
        encoding='utf-8',
        template_paths=template_paths,
    )

    if settings.ROUTER is None:
        settings.ROUTER = router_class(routes)

    response = settings.ROUTER.get_response(request)

    await send(response.start)
    await send(response.body)

    # for chunk in [b'Hello', b', ', b'world!']:
    #     await send({
    #         'type': 'http.response.body',
    #         'body': chunk,
    #         'more_body': True
    #     })

    # await send({
    #     'type': 'http.response.body',
    #     'body': b'',
    # })
