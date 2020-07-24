# PerfPythonFastAPI

## Docs
- https://morioh.com/p/78598efe32b5

## Install
```
 pip install fastapi
 
 pip install uvicorn
 
 ```
 You will also need an ASGI server, for production such as Uvicorn or Hypercorn.
 
 ##  Code "main.py"
 
 ```
 from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

 ## Run the server 
 
 uvicorn main:app --reload
