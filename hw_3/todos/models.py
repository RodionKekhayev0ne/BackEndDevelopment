from django.db import models


# Create your models here.

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    isDone = models.BooleanField(default=False)
