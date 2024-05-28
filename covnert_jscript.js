const express = require('express');
const app = express();
app.use(express.json());

let todos = [];

class Todo {
    constructor(id, task, completed = false) {
        this.id = id;
        this.task = task;
        this.completed = completed;
    }
}

app.post('/todo/', (req, res) => {
    const todo = new Todo(req.body.id, req.body.task, req.body.completed);
    todos.push(todo);
    res.json(todo);
});

app.get('/todo/', (req, res) => {
    res.json(todos);
});

app.get('/todo/:todoId', (req, res) => {
    const todo = todos.find(t => t.id === parseInt(req.params.todoId));
    if (!todo) res.status(404).send('Todo not found');
    res.json(todo);
});

app.put('/todo/:todoId', (req, res) => {
    const todo = todos.find(t => t.id === parseInt(req.params.todoId));
    if (!todo) res.status(404).send('Todo not found');
    todo.task = req.body.task;
    todo.completed = req.body.completed;
    res.json(todo);
});

app.delete('/todo/:todoId', (req, res) => {
    const todoIndex = todos.findIndex(t => t.id === parseInt(req.params.todoId));
    if (todoIndex === -1) res.status(404).send('Todo not found');
    todos.splice(todoIndex, 1);
    res.json({ message: 'Todo deleted successfully' });
});

app.listen(3000, () => console.log('Server running on port 3000'));