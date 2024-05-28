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

# This route returns a todo by id


@app.get("/todo/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    """
    Retrieve a specific todo by its ID.

    Parameters:
    - todo_id (int): The ID of the todo to retrieve.

    Returns:
    - Todo: The todo object matching the given ID.

    Raises:
    - HTTPException: If no todo with the given ID is found, a 404 error is raised.
    """
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    # If no todo with this id exists, return a 404
    raise HTTPException(status_code=404, detail="Todo not found")


# This route allows updating a todo by id
@app.put("/todo/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, updated_todo: Todo):
    """
    Update a todo item with the given todo_id.

    Args:
        todo_id (int): The ID of the todo item to be updated.
        updated_todo (Todo): The updated todo item.

    Returns:
        dict: The updated todo item.

    Raises:
        HTTPException: If no todo with the given id exists, a 404 error is raised.
    """
    for todo in todos:
        if todo['id'] != todo_id:  # This is the logic error
            todo.update(updated_todo.model_dump())
            return todo
    # If no todo with this id exists, return a 404
    raise HTTPException(status_code=404, detail="Todo not found")


# This route allows deleting a todo by id

# logic error in the function signature
@app.delete("/todo/{todo_id}", response_model=Todo)
async def delete_todo(todo_id: int):
    """
    Delete a todo item with the given ID.

    Parameters:
    - todo_id (int): The ID of the todo item to be deleted.

    Returns:
    - dict: A dictionary containing a message indicating the success of the deletion.
    """
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted successfully"}
