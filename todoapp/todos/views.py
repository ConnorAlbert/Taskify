from django.shortcuts import render, redirect
from .models import Todo
from django.shortcuts import get_object_or_404
from .forms import TodoForm
from django.db.models import Max
from django.contrib import messages
import time

app_name = 'todos'

# Dictionary to store the last time a change_todo_order request was made for each todo
last_change_request = {}

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todos = Todo.objects.all()
            max_order = todos.aggregate(Max('order'))['order__max'] or 0
            new_todo = form.save(commit=False)
            new_todo.order = max_order + 1
            new_todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    todos = Todo.objects.all()
    context = {'form': form, 'todos': todos}
    return render(request, 'todos/index.html', context)

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return redirect('todos:index')

def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        todo.task = request.POST['task']
        todo.completed = request.POST.get('completed', False) == "on"
        todo.priority = request.POST['priority']
        todo.save()
        return redirect('todos:index')

    context = {
        'todo': todo,
        'PRIORITY_CHOICES': Todo.PRIORITY_CHOICES,
    }
    return render(request, 'todos/update_todo.html', context)

def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.completed = not todo.completed
    todo.save()
    todos = Todo.objects.all()
    return redirect('todos:index')

def change_todo_order(request, todo_id, direction):
    todo = get_object_or_404(Todo, pk=todo_id)
    current_time = time.time()
    last_request_time = last_change_request.get(todo_id, 0)
    if current_time - last_request_time < 1:
        messages.error(request, 'Too many requests, try again later.')
        return redirect('todos:index')
    last_change_request[todo_id] = current_time
    todos = Todo.objects.all().order_by("order")
    todos_list = list(todos)
    current_index = todos_list.index(todo)
    if direction == 'up':
        if current_index > 0:
            todo_swap = todos_list[current_index - 1]
            todo.order, todo_swap.order = todo_swap.order, todo.order
            todo.save()
            todo_swap.save()
    else:
        if current_index < len(todos_list) - 1:
            todo_swap = todos_list[current_index + 1]
            todo.order, todo_swap.order = todo_swap.order, todo.order
            todo.save()
            todo_swap.save()
    return redirect('todos:index')