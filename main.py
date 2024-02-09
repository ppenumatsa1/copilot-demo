from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Define the FastAPI application
app = FastAPI()

# Define the Todo model using Pydantic


class Todo(BaseModel):
    id: int
    task: str
    completed: bool


# In-memory storage for Todo items
todos: List[Todo] = []

# Endpoint to create a new Todo item


@app.post("/todo/", response_model=Todo)
def create_todo(todo: Todo):
    # Check if a Todo with the same ID already exists
    for existing_todo in todos:
        if existing_todo.id == todo.id:
            # If it does, return a 400 error
            raise HTTPException(
                status_code=400, detail="Todo with this ID already exists")
    # Add the new Todo to the list
    todos.append(todo)
    return todo

# Endpoint to get all Todo items


@app.get("/todo/", response_model=List[Todo])
def read_todos():
    return todos

# Endpoint to get a specific Todo item by ID


@app.get("/todo/{todo_id}", response_model=Todo)
def read_todo(todo_id: int):
    # Find the Todo with the given ID
    for todo in todos:
        if todo.id == todo_id:
            return todo
    # If not found, return a 404 error
    raise HTTPException(status_code=404, detail="Todo not found")

# Endpoint to update a specific Todo item by ID


@app.put("/todo/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: Todo):
    # Find the Todo with the given ID
    for todo in todos:
        if todo.id == todo_id:
            # Update the Todo's task and completed status
            todo.task = todo_update.task
            todo.completed = todo_update.completed
            return todo
    # If not found, return a 404 error
    raise HTTPException(status_code=404, detail="Todo not found")

# Endpoint to delete a specific Todo item by ID


@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    # Find the Todo with the given ID
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            # Remove the Todo from the list
            todos.pop(index)
            return {"message": "Todo deleted"}
    # If not found, return a 404 error
    raise HTTPException(status_code=404, detail="Todo not found")
