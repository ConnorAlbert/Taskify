from django.shortcuts import render, redirect
from .models import Todo
from django.shortcuts import get_object_or_404, redirect
from .forms import TodoForm


app_name = 'todos'

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
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
    return redirect('todos:index')

