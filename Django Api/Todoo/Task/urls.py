from django.urls import path ,include
from . import views


app_name = "Task"
urlpatterns = [
    path('',views.sho_task,name="sho_task"),
    path('task/<int:pk>', views.TaskDtail.as_view(),name= "dtaile"),
    path('<int:pk>/delete',views.TaskDelete,name="delete_task"),

]
