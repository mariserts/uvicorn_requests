import json

from typing import Any, List, Type, Union


class Response:

    def __init__(
        self: Type,
        request: Type,
        content: Any,
        encoding: str = 'utf-8',
        headers: dict = {},
        status: int = 200,
    ) -> None:

        self._content = content
        self._encoding = encoding
        self._headers = self.parse_headers(headers)
        self._request = request
        self._status = status

    @property
    def body(self: Type,) -> dict:
        return {
            'type': 'http.response.body',
            'body': str.encode(self.content, self._encoding),
        }

    @property
    def content(self: Type) -> bytes:
        return self._content

    @property
    def default_headers(self: Type) -> List[List[bytes]]:
        return [
            [
                b'content-type',
                str(f'text/plain; charset={self._encoding}').encode()
            ]
        ]

    @property
    def headers(self: Type) -> dict:
        return self._headers

    @property
    def request(self: Type) -> Type:
        return self._request

    @property
    def start(self: dict) -> dict:
        return {
            'type': 'http.response.start',
            'status': self.status,
            'headers': self.headers,
        }

    @property
    def status(self: Type) -> int:
        return self._status

    #
    #
    #

    def parse_headers(self: Type, headers_dict: dict) -> dict:
        headers = []
        headers += self.default_headers
        for key, value in headers_dict.items():
            headers.append([
                key.encode('utf-8', 'strict'),
                value.encode('utf-8', 'strict')
            ])
        return headers

    #
    #
    #

    def create_cookie(
        self: Type,
        key: str,
        value: Any,
        max_age: Union[int, None] = None,
        expires: Union[int, None] = None,
        domain: Union[str, None] = None,
        path: Union[str, None] = '/',
        secure: bool = True,
        http_only: bool = True,
        same_site: Union[bool, None] = None,
    ) -> str:

        cookie_value = f'{key}={value}'

        if max_age is not None:
            cookie_value += f'; Max-Age={max_age}'

        if expires is not None:
            cookie_value += f'; Expires={expires}'

        if domain is not None:
            cookie_value += f'; Domain={domain}'

        if path is not None:
            cookie_value += f'; Path={path}'

        if same_site is not None:
            cookie_value += f'; SameSite={same_site}'

        if secure is True:
            cookie_value += f'; Secure'

        if http_only is True:
            cookie_value += f'; HttpOnly'

        return [
            'Set-Cookie'.encode('utf-8', 'strict'),
            cookie_value.encode('utf-8', 'strict')
        ]

    def remove_cookie(self: Type, key: str) -> None:
        self.set_cookie(key, '', max_age=-999999)

    def set_cookie(
        self: Type,
        key: str,
        value: Any,
        max_age: Union[int, None] = None,
        expires: Union[int, None] = None,
        domain: Union[str, None] = None,
        path: Union[str, None] = '/',
        secure: bool = True,
        http_only: bool = True,
        same_site: Union[bool, None] = None,
    ) -> None:

        cookie = self.create_cookie(
            key,
            value,
            max_age=max_age,
            expires=expires,
            domain=domain,
            path=path,
            secure=secure,
            http_only=http_only,
            same_site=same_site,
        )

        self._headers.append(cookie)


class JSONResponse(Response):

    @property
    def body(self: Type,) -> dict:

        if isinstance(self.content, str) is False:
            content = json.dumps(self.content)

        else:
            content = self.content

        return {
            'type': 'http.response.body',
            'body': str.encode(content, self._encoding),
        }

    @property
    def default_headers(self):
        return [
            [
                b'content-type',
                str.encode(f'application/json; charset={self._encoding}')
            ]
        ]


class TemplateResponse(Response):

    @property
    def default_headers(self):
        return [
            [
                b'content-type',
                str(f'text/html; charset={self._encoding}').encode()
            ]
        ]


class BadRequestResponse(Response):

    def __init__(
        self: Type,
        content: str = 'Bad request'
    ) -> Type:

        super().__init__(None, content, status=400)


class NotFoundResponse(Response):

    def __init__(
        self: Type,
        content: str = 'Not found'
    ) -> Type:

        super().__init__(None, content, status=404)


class NotImplementedResponse(Response):

    def __init__(
        self: Type,
        content: str = 'Method not implemented'
    ) -> Type:

        super().__init__(None, content, status=501)


class RouteNotFoundResponse(Response):

    def __init__(
        self: Type,
        content: str = 'Route not found',
    ) -> Type:

        super().__init__(None, content, status=404)


class ServerErrorResponse(Response):

    def __init__(
        self: Type,
        content: str = 'Server error',
    ) -> Type:

        super().__init__(None, content, status=500)
