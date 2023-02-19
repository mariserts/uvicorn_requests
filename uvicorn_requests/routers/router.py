from typing import List, Type

import re

from ..exceptions import RouteNotFound
from ..http.responses import (
    NotImplementedResponse,
    RouteNotFoundResponse,
    ServerErrorResponse,
)


class Router:

    _cached_paths = {}

    def __init__(
        self: Type,
        routes: List[Type],
    ) -> None:

        self.routes = routes

    def reverse(
        self: Type,
        name: str,
        kwargs: dict
    ) -> str:

        for route in self.routes:
            if route.name == name:
                return route.reverse(kwargs)

        raise RouteNotFound(name)

    def get_route_for_path(
        self: Type,
        path: str,
    ) -> Type:

        # XXXX: Cache could take all memory because all paths are stored

        try:
            self._cached_paths[path]
        except KeyError:
            pass

        for route in self.routes:

            match = re.fullmatch(route.pattern, path)

            if match is not None:

                kwargs_match = re.search(route.pattern, path)

                self._cached_paths[path] = {
                    'route': route,
                    'kwargs': match.groupdict(),
                }

                return self._cached_paths[path]

        self._cached_paths[path] = None

        return self._cached_paths[path]

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
