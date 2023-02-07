from django.shortcuts import render, redirect
from .models import Todo
from django.shortcuts import get_object_or_404, redirect

app_name = 'todos'

def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todos/index.html', context)

def add_todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        priority = request.POST.get('priority', 'low')
        Todo.objects.create(task=task, priority=priority)
        return redirect('index')
    return render(request, 'todos/add_todo.html')

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
    return redirect('todos:list_todos')

def list_todos(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todos/list_todos.html', context)