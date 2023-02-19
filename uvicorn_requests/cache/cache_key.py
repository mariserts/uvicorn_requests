from datetime import datetime, timedelta, timezone

from typing import Any, Type


class CacheKey:

    key = None
    value = None
    expires_at = None

    def __init__(
        self,
        key: str,
        value: Any,
        timeout: int = 0,
    ):

        self.key = None
        self.value = None

        if timeout > 0:
            self.expires_at = datetime.now(timezone.utc)
            self.expires_at += timedelta(seconds=timeout)
