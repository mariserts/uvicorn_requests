from typing import List, Type

from uuid import uuid4
from urllib import parse


class Request:

    id = uuid4().hex

    def __init__(
        self: Type,
        scope: dict,
        body: bytes,
        encoding: str = 'utf-8',
        template_paths: List[str] = [],
    ):

        self._body = body
        self._encoding = encoding
        self._scope = scope
        self._template_paths = template_paths

    @property
    def body(self):

        if self.__body is not None:
            return self.__body

        body = b''

        if self.method == 'post':
            body = self._body
        elif self.method == 'get':
            body = self._scope['query_string']

        decoded_body = body.decode(self.encoding, 'strict')
        clean_string = urllib.parse.unquote(decoded_body)

        out = {}

        for value in clean_string.split('&'):
            if '=' in value:
                parts = value.split('=')
                out[parts[0]] = parts[1]

        self.__body = out

        return self.__body

    @property
    def cookies(self):

        value = self.headers.get('cookie', '')
        _cookies = value.split(';')

        cookies = {}

        for cookie in _cookies:
            if '=' in cookie:
                parts = cookie.split('=')
                cookies[parts[0].strip()] = parts[1].strip()

        return cookies

    @property
    def encoding(self):
        return self._encoding

    @property
    def headers(self):

        _headers = self._scope['headers']

        headers = {}

        for header in _headers:
            key = header[0].decode('utf-8')
            value = header[1].decode('utf-8')
            headers[key] = value

        return headers

    @property
    def method(self):
        return self._scope['method'].lower()

    @property
    def path(self):
        return self._scope['path']

    @property
    def template_paths(self):
        return self._template_paths

    @property
    def type(self):
        return self._scope['type']
