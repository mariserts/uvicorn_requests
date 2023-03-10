# -*- coding: utf-8 -*-
from typing import List, Type

from jinja2 import Environment, FileSystemLoader, select_autoescape


class Jinja2TemplateEngine:

    _cached_env = None
    _cached_templates = {}

    def __init__(
        self: Type,
        encoding: str = 'utf-8',
        template_paths: List[str] = [],
    ):
        self.encoding = encoding
        self.template_paths = template_paths

    @property
    def environment(
        self: Type,
    ) -> Type:

        if self._cached_env is not None:
            return self._cached_env

        self._cached_env = Environment(
            loader=FileSystemLoader(
                self.template_paths,
                encoding=self.encoding
            ),
            autoescape=select_autoescape()
        )

        return self._cached_env

    # @lru_cache(maxsize=None)
    # def get_template(
    #     self: Type,
    #     template: str,
    # ) -> Type:
    #     return self.environment.get_template(template)

    def get_template(
        self: Type,
        template: str,
    ) -> Type:

        try:
            return self._cached_templates[template]
        except KeyError:
            pass

        _template = self.environment.get_template(template)

        self._cached_templates[template] = _template

        return _template

    def render(
        self: Type,
        template_path: str,
        context: dict = {},
    ) -> str:
        return self.get_template(template_path).render(**context)
