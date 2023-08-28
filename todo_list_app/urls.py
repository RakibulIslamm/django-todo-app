from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('add-task/', views.AddTask, name='add_task'),
    path('show-tasks/', views.ShowTask, name='show_tasks'),
    path('completed-tasks/', views.ShowCompletedTask, name='completed_tasks'),
    path('edit-task/<int:id>', views.EditTask, name='edit_tasks'),
    path('complete-task/<int:id>', views.TaskCompleted, name='complete_tasks'),
    path('delete-task/<int:id>', views.DeleteTask, name='delete_tasks'),
]
