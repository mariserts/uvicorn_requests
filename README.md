# Uvicorn requests

Trying to benchmark minimal server setup against Flask, Django, NodeJS


## Benchmarks


### Uvicorn / Gunicorn config
- workers 1
- keep-alive 5


### Locust

- 100 concurrent users

locustfile.py
```
from locust import HttpUser, task

class HelloWorld(HttpUser):

    @task
    def hello_world(self):
        self.client.get('/')
```


### Uvicorn benchmark app

- RPS ~1700
- Response 95% percentile: 75ms
- Response median: 55ms


Run:
```
uvicorn demo.app:app --workers 1
```

### NodeJS benchmark app

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


### Django benchmark app

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

### Flask benchmark app

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
