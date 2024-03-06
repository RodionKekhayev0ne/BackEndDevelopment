from django.db import models
from django.db.models import CASCADE


class Todo_list(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(Todo_list, on_delete=CASCADE)
