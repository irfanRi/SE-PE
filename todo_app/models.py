from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=40)
    taskDescription = models.CharField(max_length=100)
    is_Completed = models.BooleanField(default=False)
     