from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Task
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_tasks(request):
    tasks = Task.objects.all()
    if not tasks:
        raise Http404("Tasks does not exist")
    return render(request, "tasks.html", context={"tasks": tasks})


def task_detail_view(request, id):
    task = get_object_or_404(Task, id)
    return render(request, 'task_detail.html', context={'task': task})




