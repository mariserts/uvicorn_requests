# Uvicorn requests

Trying to benchmark minimal server setup against Flask and Django


## Uvicorn / Gunicorn config
- workers 1
- keep-alive 5


## Locust

- 100 concurrent users
- 10 spawn rate

locustfile.py
```
from locust import HttpUser, task

class HelloWorld(HttpUser):

    @task
    def hello_world(self):
        self.client.get('/')
```


## Uvicorn benchmark app

Run:
```
uvicorn demo.app:app --workers 1
```


## Django benchmark app

Run:
```
gunicorn app.wsgi --workers 1 --keep-alive 5
```

urls.py
```
from django.shortcuts import render
from django.urls import path

def HomePageFuncView(request):

    return render(
        request,
        'base.html',
        context={
            'request': request
        }
    )

urlpatterns = [
    path('', HomePageFuncView, name='home'),
]
```

base.html
```
<h1>Hello world</h1>
{{ request }}
```

## Flask benchmark app

Run:
```
gunicorn app.app --workers 1 --keep-alive 5
```

app.py
```
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', request=request)
```

index.html
```
<h1>Hello world</h1>
{{ request }}
```
