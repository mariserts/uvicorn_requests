from typing import List, Type

from jinja2 import Environment, FileSystemLoader, select_autoescape


class Jinja2TemplateEngine:

    def __init__(
        self: Type,
        encoding: str = 'utf-8',
        template_paths: List[str] = [],
    ):
        self._encoding = encoding
        self._template_paths = template_paths

    @property
    def encoding(
        self: Type,
    ) -> str:

        return self._encoding

    @property
    def environment(
        self: Type,
    ) -> Type:

        return Environment(
            loader=FileSystemLoader(
                self.template_paths,
                encoding=self.encoding
            ),
            autoescape=select_autoescape()
        )

    @property
    def template_paths(
        self: Type,
    ) -> str:

        return self._template_paths

    #
    #
    #

    def get_template(
        self: Type,
        template_path: str,
    ) -> Type:

        return self.environment.get_template(template_path)

    def render(
        self: Type,
        template_path: str,
        context: dict = {},
    ) -> str:

        template = self.get_template(template_path)

        return template.render(**context)
