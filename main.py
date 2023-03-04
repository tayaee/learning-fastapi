import uvicorn
from fastapi import FastAPI

from models import Todo
from models import session

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print('Starting up')


@app.get('/')
def home():
    todos_query = session.query(Todo)
    todos = todos_query.all()
    return todos


@app.post('/create')
async def create_todo(text: str, is_complete: bool = False):
    todo = Todo(text=text, is_done=is_complete)
    session.add(todo)
    session.commit()
    return {'todo added': todo.text}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=5001, reload=True)
