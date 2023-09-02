from django.shortcuts import render,redirect
from todo_app.forms import TaskForm
from todo_app.models import TaskModel
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('show_tasks')
    else:
        task = TaskForm()
    return render(request,'add_task.html',{'form': task})

def show_tasks(request):
    task = TaskModel.objects.all()  
    return render(request,'show_tasks.html',{'data':task})

def edit_task(request,id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        task = TaskForm(request.POST,instance=task)
        if task.is_valid():
            task.save()
            return redirect('show_tasks')
    return render(request,'edit_task.html',{'form': form})
    
def delete_tasks(request,id):
    task = TaskModel.objects.get(pk = id).delete()
    return redirect('show_tasks')


def complete_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task.is_Completed = True
    task.save()
    return redirect('completed_task')

def completed_task(request):
    task = TaskModel.objects.filter(is_Completed = True)
    return render(request, 'completed_tasks.html',{'data':task})

def delete_completed_task(request,id):
    task = TaskModel.objects.get(pk = id).delete()
    return redirect('completed_task')