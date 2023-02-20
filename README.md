# Uvicorn requests

Trying to benchmark minimal server setup against Flask, Django, NodeJS


## 1. Benchmarks


### 1.1 Uvicorn / Gunicorn config
- workers 1
- keep-alive 5

### 1.2 Locust

- 100 concurrent users

locustfile.py
```
from locust import HttpUser, task

class HelloWorld(HttpUser):

    @task
    def hello_world(self):
        self.client.get('/')
```

### 1.3 Uvicorn requests benchmark app

App is located in /demo/

- RPS ~1700
- Response 95% percentile: 75ms
- Response median: 55ms

Run:
```
uvicorn demo.app:app --workers 1
```

### 1.4 Plain uvicorn app

- RPS ~1760
- Response 95% percentile: 60ms
- Response median: 44ms

Run:
```
uvicorn demo.app:app --workers 1
```

app.py
```
async def app(scope, receive, send):

    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': b'<h1>Hello, world!</h1>' + str(scope).encode(),
    })
```


### 1.5 NodeJS benchmark app

- RPS ~1750
- Response 95% percentile: 63ms
- Response median: 43ms

Run
```
node app.js
```

app.js
```
const express = require('express');
const app = express();


app.set('view engine', 'ejs');


app.get('/' , (req , res) => {
    res.render('index' , {
        request : req
    });
})

app.listen(3000 , ()=>{
    console.log('server is running on port 3000');
})
```

index.ejs
```
<h1>Hello world</h1>
<%= request %>
```

### 1.6 Flask benchmark app

- RPS ~1100

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

### 1.7 Django benchmark app

- RPS ~1000

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
