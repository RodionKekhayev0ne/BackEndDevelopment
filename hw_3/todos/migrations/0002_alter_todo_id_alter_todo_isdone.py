# Generated by Django 5.0.2 on 2024-02-22 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]