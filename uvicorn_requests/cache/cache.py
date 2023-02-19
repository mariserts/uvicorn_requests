from datetime import datetime, timezone

from typing import Any, Type

from .cache_key import CacheKey


class Cache:

    def get(
        self: Type,
        key: str,
        default: Any = None
    ) -> None:

        return None

    def set(
        self: Type,
        key: str,
        value: Any,
        timeout: int = 0,
    ) -> None:

        pass


class SimpleCache(Cache):

    keys = {}

    def get(
        self: Type,
        key: str,
        default: Any = None
    ) -> Any:

        try:
            key = self.keys[key]
        except KeyError:
            return default

        expires_at = key.expires_at

        if expires_at is None:
            return key.value

        if key.expires_at < datetime.now(timezone.utc):
            self.remove(key)
            return default

        return key.value

    def set(
        self: Type,
        key: str,
        value: Any,
        timeout: int = 0,
    ) -> None:

        self.keys[key] = CacheKey(key, value, timeout)

    def clear(
        self: Type,
    ) -> None:

        self.keys = {}

    def remove(
        self: Type,
        key: str,
    ) -> None:

        try:
            del self.keys[key]
        except KeyError:
            pass
