from django.shortcuts import render, redirect
from .models import Taskify
from django.shortcuts import get_object_or_404
from .forms import TaskifyForm
from django.db.models import Max
from django.contrib import messages
import time

app_name = 'taskify'

# Dictionary to store the last time a change_taskify_order request was made for each taskify
last_change_request = {}

def index(request):
    if request.method == 'POST':
        form = TaskifyForm(request.POST)
        if form.is_valid():
            taskify_list = Taskify.objects.all()
            max_order = taskify_list.aggregate(Max('order'))['order__max'] or 0
            new_taskify = form.save(commit=False)
            new_taskify.order = max_order + 1
            new_taskify.save()
            return redirect('taskify:index')
    else:
        form = TaskifyForm()
    taskify_list = Taskify.objects.all()
    context = {'form': form, 'taskify_list': taskify_list, 'PRIORITY_CHOICES': Taskify.PRIORITY_CHOICES}
    return render(request, 'taskify/index.html', context)

def delete_taskify(request, pk):
    taskify = get_object_or_404(Taskify, id=pk)
    taskify.delete()
    return redirect('taskify:index')

def update_taskify(request, pk):
    taskify = Taskify.objects.get(id=pk)

    if request.method == 'POST':
        taskify.task = request.POST['task']
        taskify.completed = request.POST.get('completed', False) == "on"
        taskify.priority = request.POST['priority']
        taskify.save()
        return redirect('taskify:index')

    context = {
        'taskify': taskify,
        'PRIORITY_CHOICES': Taskify.PRIORITY_CHOICES,
    }
    return render(request, 'taskify/update_taskify.html', context)

def toggle_taskify(request, taskify_id):
    taskify = get_object_or_404(Taskify, pk=taskify_id)
    taskify.completed = not taskify.completed
    taskify.save()
    return redirect('taskify:index')

def change_taskify_order(request, taskify_id, direction):
    taskify = get_object_or_404(Taskify, pk=taskify_id)
    current_time = time.time()
    last_request_time = last_change_request.get(taskify_id, 0)
    if current_time - last_request_time < 1:
        messages.error(request, 'Too many requests, try again later.')
        return redirect('taskify:index')
    last_change_request[taskify_id] = current_time
    taskify_list = Taskify.objects.all().order_by("order")
    taskify_list = list(taskify_list)
    current_index = taskify_list.index(taskify)
    if direction == 'up':
        if current_index > 0:
            taskify_swap = taskify_list[current_index - 1]
            taskify.order, taskify_swap.order = taskify_swap.order, taskify.order
            taskify.save()
            taskify_swap.save()
    else:
        if current_index < len(taskify_list) - 1:
            taskify_swap = taskify_list[current_index + 1]
            taskify.order, taskify_swap.order = taskify_swap.order, taskify.order
            taskify.save()
            taskify_swap.save()
    return redirect('taskify:index')

def filter_by_priority(request):
    selected_priority = request.GET.get('priority')
    if selected_priority:
        taskify_list = Taskify.objects.filter(priority=selected_priority)
    else:
        taskify_list = Taskify.objects.all()
    context = {'taskify_list': taskify_list, 'selected_priority': selected_priority, 'PRIORITY_CHOICES': Taskify.PRIORITY_CHOICES}
    return render(request, 'taskify/index.html', context)
