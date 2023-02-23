# Uvicorn requests


## Minimal app

app.py
```python

from uvicorn_requests.app import app as uvicorn_requests_app
from uvicorn_requests.http.responses import JSONResponse
from uvicorn_requests.routers.route import Route
from uvicorn_requests.viewsets.viewset import ViewSet, TemplateViewSet


class HtmlViewSet(TemplateViewSet):
    def get(self, request):
        return self.render(request, 'base.html', context=self.get_context())


class ApiViewSet(ViewSet):
    def get(self, request):
        return JSONResponse(request, {'data': 'data'})


ROUTES = [
    Route(r'/api/', ApiViewSet, name='api'),
    Route(r'/', HtmlViewSet, name='html'),
]


TEMPLATE_PATHS = [
    '/templates/'
]


async def app(scope, receive, send):
    await uvicorn_requests_app(
        scope,
        receive,
        send,
        routes=ROUTES,
        template_paths=TEMPLATE_PATHS
    )
```

Run:
```
uvicorn app:app
```
