from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from .forms import TaskForm



@csrf_exempt
def get_tasks(request):
    tasks = Task.objects.all()
    if not tasks:
        raise Http404("Tasks does not exist")
    return render(request, "tasks.html", context={"tasks": tasks})


def task_detail_view(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'task_detail.html', context={'task': task})


def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')

    return render(request, 'task-create.html', {
        'form': TaskForm(),
    })


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task-edit.html',{'form': form, 'task': task})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')

    return render(request, 'task-delete.html', {'task': task})


