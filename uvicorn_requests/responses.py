from typing import Any, Type, Union


class Response:

    encoding = 'utf-8'
    default_headers = [
        [
            b'content-type',
            b'text/plain; charset=utf-8'
        ]
    ]

    def __init__(
        self: Type,
        request: Type,
        content: Any,
        status: int = 200,
        headers: dict = {}
    ):

        self._request = request
        self._content = content
        self._status = status
        self._headers = self.parse_headers(headers)

    @property
    def content(
        self: Type
    ) -> bytes:

        return self._content

    @property
    def headers(
        self: Type
    ) -> dict:

        return self._headers

    @property
    def request(
        self: Type
    ) -> Type:

        return self._request

    @property
    def status(
        self: Type
    ) -> int:

        return self._status

    #
    #
    #

    @property
    def start(
        self: dict
    ) -> dict:
        return {
            'type': 'http.response.start',
            'status': self.status,
            'headers': self.headers,
        }

    @property
    def body(
        self: Type,
    ) -> dict:
        return {
            'type': 'http.response.body',
            'body': self.get_body(),
        }

    # --

    def parse_headers(
        self: Type,
        headers_dict: dict
    ) -> dict:

        headers = []
        headers += self.get_default_headers()

        for key, value in headers_dict.items():
            headers.append([
                key.encode('utf-8', 'strict'),
                value.encode('utf-8', 'strict')
            ])

        return headers

    # --

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

    def create_cookie(
        self,
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

    def get_body(
        self: Type
    ) -> str:

        return str.encode(self.content, self.encoding)

    def get_default_headers(
        self: Type
    ) -> dict:

        return self.default_headers
