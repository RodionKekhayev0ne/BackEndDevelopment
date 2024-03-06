# Generated by Django 5.0.2 on 2024-03-06 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todo_id_alter_todo_isdone'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_list',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='todos.todolist'),
        ),
    ]