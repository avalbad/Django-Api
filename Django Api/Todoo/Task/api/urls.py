from django.urls import path
from Task.api.views import get_all_tasks , get_task ,update_view

urlpatterns = [
    path('tasks/',get_all_tasks,name = 'task_list'),
    path('task/<int:pk>' , get_task , name= "task_dtail"),
    path('task/<int:pk>/update', update_view , name="task_update")
]