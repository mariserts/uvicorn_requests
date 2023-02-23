from typing import Type

from uvicorn_requests.http.responses import JSONResponse
from uvicorn_requests.viewsets.viewset import TemplateViewSet


class HomePageViewSet(TemplateViewSet):

    def get(
        self: Type,
        request: Type
    ):

        return self.render(
            request,
            'base.html',
            context=self.get_context(),
        )


class JSONRootViewSet(TemplateViewSet):

    def get(
        self: Type,
        request: Type
    ):

        return JSONResponse(
            request,
            {
                'data': 'data'
            }
        )


class JSONDetailViewSet(TemplateViewSet):

    def get(
        self: Type,
        request: Type,
        pk: int,
    ):

        return JSONResponse(
            request,
            {
                'pk': pk
            }
        )
