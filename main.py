from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create a new FastAPI instance
app = FastAPI()

# This list will hold our todos
todos = []

# This class defines the data model for a todo


class Todo(BaseModel):
    id: int
    task: str
    completed: Optional[bool] = False

# This route allows creating a new todo


@app.post("/todo/", response_model=Todo)
async def create_todo(todo: Todo):
    todos.append(todo.model_dump())
    return todo

# This route returns all todos


@app.get("/todo/", response_model=list[Todo])
async def get_todos():
    return todos

# This route returns a todo by id


@app.get("/todo/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    # If no todo with this id exists, return a 404
    raise HTTPException(status_code=404, detail="Todo not found")

# This route allows updating a todo by id


@app.put("/todo/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: Todo):
    for index, t in enumerate(todos):
        if t['id'] == todo_id:
            todos[index] = todo.model_dump()
            return todo
    # If no todo with this id exists, return a 404
    raise HTTPException(status_code=404, detail="Todo not found")

# This route allows deleting a todo by id


@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    for index, t in enumerate(todos):
        if t['id'] == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted"}
    # If no todo with this id exists, return a 404
    raise HTTPException(status_code=404, detail="Todo not found")
