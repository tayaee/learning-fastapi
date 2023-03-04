import uvicorn
from fastapi import FastAPI

from models import Todo
from models import session

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print('Starting up')


@app.post('/todos')
async def create_todo(text: str, is_complete: bool = False):
    todo = Todo(text=text, is_done=is_complete)
    session.add(todo)
    session.commit()
    return {'todo added': todo.text}


@app.get('/todos')
async def get_todos():
    todos_query = session.query(Todo)
    todos = todos_query.all()
    return todos


@app.get('/todos/{id}')
async def get_todo(id: int):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    return todo


@app.get('/todos?done=true')
async def list_done_todos():
    todos_query = session.query(Todo).filter(Todo.is_done == True)
    todos = todos_query.all()
    return todos


@app.put('/todos/{id}')
async def update_todo(id: int, new_text: str = "", is_complete: bool = False):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    if new_text:
        todo.text = new_text
    todo.is_done = is_complete
    session.add(todo)
    session.commit()
    return {'message': 'OK'}


@app.delete('/todos/{id}')
async def delete_todo(id: int):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    if todo:
        session.delete(todo)
        session.commit()
        return {'message': f'deleted {todo.id}'}
    else:
        return {'message': f'{id} not found'}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=5001, reload=True)
