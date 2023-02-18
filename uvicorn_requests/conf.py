from typing import Any, List, Type


class Settings:

    _TEMPLATE_ENGINE = None

    @property
    def TEMPLATE_ENGINE(
        self: Type
    ) -> Type:

        if self._TEMPLATE_ENGINE is not None:
            return self._TEMPLATE_ENGINE

        return self.TEMPLATE_ENGINE_CLASS()

    @property
    def TEMPLATE_ENGINE_CLASS(
        self: Type
    ) -> Type:

        # XXXX Import issue: Do this thing better
        from .template_engines.jinja2 import Jinja2TemplateEngine

        return Jinja2TemplateEngine

    @property
    def TEMPLATE_PATHS(
        self: Type
    ) -> List[str]:

        return getattr(self, '_TEMPLATE_PATHS', [])

    def set(
        self: Type,
        attribute_name: str,
        value: Any
    ) -> None:

        setattr(self, attribute_name, value)


settings = Settings()
