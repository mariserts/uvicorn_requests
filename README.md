# Uvicorn requests


## Install from github

```
pip install https://github.com/mariserts/uvicorn_requests/archive/refs/heads/main.zip
```

## Minimal app

app.py
```python

from uvicorn_requests.app import app as uvicorn_requests_app
from uvicorn_requests.http.responses import JSONResponse
from uvicorn_requests.routers.route import Route
from uvicorn_requests.viewsets.viewset import ViewSet


class ApiViewSet(ViewSet):
    def get(self, request):
        return JSONResponse(request, {'data': 'data'})


ROUTES = [
    Route(r'/', ApiViewSet, name='api'),
]


async def app(scope, receive, send):
    await uvicorn_requests_app(
        scope,
        receive,
        send,
        routes=ROUTES,
    )
```

Run:
```
uvicorn app:app
```
