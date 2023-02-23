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

        self.name = name
        self.pattern = re.compile(self.clean_pattern(pattern))
        self.view = view

    def clean_pattern(
        self: Type,
        pattern: str,
    ) -> str:

        if pattern == r'':
            pattern = r'/'

        return pattern
