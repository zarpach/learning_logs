from django.urls import path
import tasks.views

urlpatterns = [
    path('', tasks.views.get_tasks, name='task-list'),
    path('<int:pk>/', tasks.views.task_detail_view, name='task-detail'),
    path('create/', tasks.views.task_create_view, name='task-create'),
    path('edit/<int:pk>', tasks.views.edit_task, name='task-edit'),
    path('delete/<int:pk>', tasks.views.task_delete_view, name='task-delete')
]
