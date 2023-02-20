# -*- coding: utf-8 -*-
import re

from typing import List, Type

from ..http.responses import (
    NotImplementedResponse,
    RouteNotFoundResponse,
    ServerErrorResponse,
)


class Router:

    def __init__(
        self: Type,
        routes: List[Type],
    ) -> None:

        self.routes = routes

    def get_route_for_path(
        self: Type,
        path: str,
    ) -> Type:

        for route in self.routes:

            match = re.fullmatch(route.pattern, path)

            if match is not None:

                return {
                    'route': route,
                    'kwargs': match.groupdict(),
                }

        return None

    def get_response(
        self: Type,
        request: Type,
    ) -> Type:

        data = self.get_route_for_path(request.path)
        if data is None:
            return RouteNotFoundResponse()

        route = data['route']
        kwargs = data['kwargs']

        view = route.view

        if request.method not in view.HTTP_METHODS:
            return NotImplementedResponse()

        view_method = hasattr(view, request.method)

        if view_method is False:
            return NotImplementedResponse()

        try:
            response = getattr(
                view(),
                request.method
            )(
                request,
                **kwargs
            )

        except Exception as e:
            return ServerErrorResponse(str(e))

        return response
