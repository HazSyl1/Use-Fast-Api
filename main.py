import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return{'message':'Hello, stranger'}


@app.get('/Welcome')
def get_name(name:str):
    return{'Welcome to this site' : f'{name}'}


if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000,debug=True)
    