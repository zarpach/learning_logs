from django.urls import path
import tasks.views

urlpatterns = [
    path('', tasks.views.get_tasks),
]
