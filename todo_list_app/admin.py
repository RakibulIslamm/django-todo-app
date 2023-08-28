from django.contrib import admin
from todo_list_app.models import TaskModel

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'taskTitle', 'taskDescription']

admin.site.register(TaskModel,TaskModelAdmin)
