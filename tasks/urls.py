from django.urls import path
import tasks.views

urlpatterns = [
    path('', tasks.views.get_tasks),
    path('<int:pk>', tasks.views.task_detail_view, name='task-detail')
]
