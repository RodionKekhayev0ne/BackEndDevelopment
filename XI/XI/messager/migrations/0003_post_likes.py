# Generated by Django 5.0.4 on 2024-04-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messager', '0002_remove_post_owner_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]