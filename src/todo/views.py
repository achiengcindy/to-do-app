from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm


def index(request):
    todo_list = Task.objects.all()[:7]
    context = {'tasks': todo_list}
    return render (request, 'todo/task/index.html', context)


def create_task(request):
    if request.method == 'POST':
        add_form =TaskForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('index')
    else:
        add_form =TaskForm()
    context= {'form':add_form}
    return render(request, 'todo/task/create.html', context )
	
	
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')
   