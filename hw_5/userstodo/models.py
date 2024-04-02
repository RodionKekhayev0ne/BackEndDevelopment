from django.db import models
from django.db.models import CASCADE


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Todos(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    status = models.BooleanField(default=False)

