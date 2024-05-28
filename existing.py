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
    """
    Create a new todo item.

    Args:
        todo (Todo): The todo item to be created.

    Returns:
        Todo: The created todo item.
    """
    todos.append(todo.model_dump())
    return todo

# This route returns all todos


@app.get("/todo/", response_model=list[Todo])
async def get_todos():
    """
    Retrieve a list of todos.

    Returns:
        list[Todo]: A list of todos.
    """
    return todos

# This route returns a single todo


@app.get("/todo/{todo_id}", response_model=Todo)
async def get_todo_by_id(todo_id: int):
    """
    Retrieve a todo by its ID.

    Args:
        todo_id (int): The ID of the todo to retrieve.

    Returns:
        Todo: The todo item with the specified ID.
    """
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# This route allows updating a todo
@app.put("/todo/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: Todo):
    for index, t in enumerate(todos):
        if t['id'] == todo_id:
            todos[index] = todo.model_dump()
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# This route allows deleting a todo


@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    for index, t in enumerate(todos):
        if t['id'] == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted"}
    # If no todo with this id exists, return a 404
    raise HTTPException(status_code=404, detail="Todo not found")
