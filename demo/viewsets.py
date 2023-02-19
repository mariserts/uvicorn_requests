from typing import Type

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
