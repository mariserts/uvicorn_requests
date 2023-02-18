from typing import Type


class RouteNotFound(Exception):

    def __init__(
        self: Type,
        route_name: str
    ) -> None:

        self.message = f'Route for name "{route_name}" not found'
