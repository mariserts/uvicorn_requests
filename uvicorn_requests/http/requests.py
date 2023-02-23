# -*- coding: utf-8 -*-
from typing import List, Type

from uuid import uuid4
from urllib import parse

from ..conf import settings
from ..template_engines.jinja2 import Jinja2TemplateEngine


class Request:

    id = uuid4().hex

    _cached_body = None
    _cached_cookies = None
    _cached_headers = None

    def __init__(
        self: Type,
        scope: dict,
        body: bytes,
        encoding: str = 'utf-8',
        template_paths: List[str] = [],
        template_engine_class: Type = Jinja2TemplateEngine,
    ):

        self._body = body
        self._scope = scope

        self.encoding = encoding
        self.method = self._scope['method'].lower()
        self.path = self.clean_path(self._scope['path'])
        self.template_engine_class = template_engine_class
        self.template_paths = template_paths
        self.type = self._scope['type']

        self.settings = settings

    @property
    def body(
        self: Type,
    ) -> bytes:

        if self._cached_body is not None:
            return self._cached_body

        body = b''

        if self.method == 'post':
            body = self._body
        elif self.method == 'get':
            body = self._scope['query_string']

        decoded_body = body.decode(self.encoding, 'strict')
        clean_string = parse.unquote(decoded_body)

        out = {}

        for value in clean_string.split('&'):
            if '=' in value:
                parts = value.split('=')
                out[parts[0]] = parts[1]

        self._cached_body = out

        return self._cached_body

    @property
    def cookies(
        self: Type,
    ) -> dict:

        if self._cached_cookies is not None:
            return self._cached_cookies

        value = self.headers.get('cookie', '')
        _cookies = value.split(';')

        cookies = {}

        for cookie in _cookies:
            if '=' in cookie:
                parts = cookie.split('=')
                cookies[parts[0].strip()] = parts[1].strip()

        self._cached_cookies = cookies

        return self._cached_cookies

    @property
    def headers(
        self: Type,
    ) -> dict:

        if self._cached_headers is not None:
            return self._cached_headers

        _headers = self._scope['headers']

        headers = {}

        for header in _headers:
            headers[header[0].decode('utf-8')] = header[1].decode('utf-8')

        self._cached_headers = headers

        return self._cached_headers

    def clean_path(
        self: Type,
        path: str
    ) -> str:

        if path.endswith('/') is True:
            return path

        return path + '/'
