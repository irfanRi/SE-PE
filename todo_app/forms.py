from django import forms
from todo_app.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude = ['is_Completed']
        fields = ['taskTitle', 'taskDescription']