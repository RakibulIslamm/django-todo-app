from django import forms
from todo_list_app.models import TaskModel


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
        labels = {
            'taskTitle': ('Title'),
            'taskDescription': ('Description'),
        }
        
class EditTaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription', 'is_completed']
        labels = {
            'taskTitle': ('Title'),
            'taskDescription': ('Description'),
        }

