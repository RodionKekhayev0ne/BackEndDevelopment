# Generated by Django 5.0.2 on 2024-03-06 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0015_todo_list_delete_todolist_todo_todo_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='todo_list',
        ),
    ]