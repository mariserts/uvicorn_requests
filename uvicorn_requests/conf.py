# -*- coding: utf-8 -*-
from typing import Type


class Settings:

    _ROUTER = None
    _TEMPLATE_ENGINE = None
    _TEMPLATE_ENGINE_CLASS = None
    _TEMPLATE_PATHS = []

    #
    #
    #

    @property
    def ROUTER(
        self: Type
    ) -> Type:

        return self._ROUTER

    @ROUTER.setter
    def ROUTER(
        self: Type,
        value: Type,
    ) -> None:

        self._ROUTER = value

    #
    #
    #

    @property
    def TEMPLATE_ENGINE(
        self: Type
    ) -> Type:

        return self._TEMPLATE_ENGINE

    @TEMPLATE_ENGINE.setter
    def TEMPLATE_ENGINE(
        self: Type,
        value: Type,
    ) -> Type:

        self._TEMPLATE_ENGINE = value

    @property
    def TEMPLATE_ENGINE_CLASS(
        self: Type
    ) -> Type:

        if self._TEMPLATE_ENGINE_CLASS is not None:
            return self._TEMPLATE_ENGINE_CLASS

        # XXXX Import issue: Do this thing better
        from .template_engines.jinja2 import Jinja2TemplateEngine

        self._TEMPLATE_ENGINE_CLASS = Jinja2TemplateEngine

        return self._TEMPLATE_ENGINE_CLASS

    @TEMPLATE_ENGINE_CLASS.setter
    def TEMPLATE_ENGINE_CLASS(
        self: Type,
        value: Type,
    ) -> Type:

        self._TEMPLATE_ENGINE_CLASS = value


settings = Settings()
