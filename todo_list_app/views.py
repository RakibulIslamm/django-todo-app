from django.shortcuts import render, redirect
from todo_list_app.forms import TaskModelForm, EditTaskModelForm
from todo_list_app.models import TaskModel

# Create your views here.
def Home(req):
    return render(req, 'home.html')

def AddTask(req):
    if req.method == 'POST':
        form = TaskModelForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
            return redirect('/show-tasks')
    else:
        form = TaskModelForm()
    return render(req, 'add_task.html', {'todo_form':form})

def ShowTask(req):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(req, 'show_tasks.html', {'tasks': tasks})

def ShowCompletedTask(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})

def EditTask(req, id):
    task = TaskModel.objects.get(pk=id)
    form = EditTaskModelForm(instance=task)
    if req.method == 'POST':
        form = EditTaskModelForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            if form.cleaned_data['is_completed']:
                return redirect('/completed-tasks')
            else:
                return redirect('/show-tasks')
    return render(req, 'edit_task.html', {"todo_form":form})

def TaskCompleted(req, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')


def DeleteTask(req, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    if task.is_completed:
        return redirect('completed_tasks')
    else:
        return redirect('show_tasks')
            
    
