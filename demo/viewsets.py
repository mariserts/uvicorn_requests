from typing import Type

from uvicorn_requests.http.responses import TemplateResponse
from uvicorn_requests.viewsets.viewset import ViewSet


class HomePageViewSet(ViewSet):

    def get(
        self: Type,
        request: Type
    ):

        return TemplateResponse(request, '<h1>Hello world</h1>')
