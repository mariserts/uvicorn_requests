from typing import List, Type

from ..http.responses import NotImplementedResponse, TemplateResponse


class ViewSet:

    HTTP_METHOD_DELETE = 'delete'
    HTTP_METHOD_GET = 'get'
    HTTP_METHOD_HEAD = 'head'
    HTTP_METHOD_OPTIONS = 'options'
    HTTP_METHOD_PATCH = 'patch'
    HTTP_METHOD_POST = 'post'
    HTTP_METHOD_PUT = 'put'

    HTTP_METHODS = [
        HTTP_METHOD_DELETE,
        HTTP_METHOD_GET,
        HTTP_METHOD_OPTIONS,
        HTTP_METHOD_PATCH,
        HTTP_METHOD_POST,
        HTTP_METHOD_PUT,
    ]

    NOT_IMPLEMENTED_MESSEGE = 'Method is not implemented'

    def __init__(
        self: Type,
        request: Type,
    ) -> None:

        self.request = request

    def delete(
        self: Type,
        request: Type,
        *args: List,
        **kwargs: dict
    ) -> Type:

        return NotImplementedResponse(self.NOT_IMPLEMENTED_MESSEGE)

    def get(
        self: Type,
        request: Type,
        *args: List,
        **kwargs: dict
    ) -> Type:

        return NotImplementedResponse(self.NOT_IMPLEMENTED_MESSEGE)

    def head(
        self: Type,
        request: Type,
        *args: List,
        **kwargs: dict
    ) -> Type:

        return NotImplementedResponse(self.NOT_IMPLEMENTED_MESSEGE)

    def options(
        self: Type,
        request: Type,
        *args: List,
        **kwargs: dict
    ) -> Type:

        return NotImplementedResponse(self.NOT_IMPLEMENTED_MESSEGE)

    def patch(
        self: Type,
        request: Type,
        *args: List,
        **kwargs: dict
    ) -> Type:

        return NotImplementedResponse(self.NOT_IMPLEMENTED_MESSEGE)

    def post(
        self: Type,
        request: Type,
        *args: List,
        **kwargs: dict
    ) -> Type:

        return NotImplementedResponse(self.NOT_IMPLEMENTED_MESSEGE)

    def put(
        self: Type,
        request: Type,
        *args: List,
        **kwargs: dict
    ) -> Type:

        return NotImplementedResponse(self.NOT_IMPLEMENTED_MESSEGE)

    #
    #
    #

    def get_context(
        self: Type,
    ) -> dict:

        return {
            'request': self.request
        }

    def render(
        self: Type,
        request: Type,
        template_path: str,
        context: dict = {},
        encoding: str = 'utf-8',
        headers: dict = {},
        status: int = 200,
    ) -> str:

        return TemplateResponse(
            request=request,
            template_path=template_path,
            context=context,
            encoding=request.encoding,
            headers=headers,
            status=status,
            template_paths=request.template_paths
        )
