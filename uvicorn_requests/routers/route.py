# -*- coding: utf-8 -*-
import re

from typing import Type


class Route:

    def __init__(
        self: Type,
        pattern: str,
        view: Type,
        name: str = None
    ) -> None:

        self._pattern = re.compile(self.clean_pattern(pattern))
        self._view = view
        self._name = name

    @property
    def name(
        self: Type
    ) -> str:
        return self._name

    @property
    def pattern(
        self: Type
    ) -> str:
        return re.compile(self._pattern)

    @property
    def view(
        self: Type
    ) -> Type:
        return self._view

    def clean_pattern(
        self: Type,
        pattern: str,
    ) -> str:
        if pattern == r'':
            pattern = r'/'
        return pattern
