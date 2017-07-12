from django.db import models

# Create your models here.

class ToDoList(models.Model) :
    activity = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
