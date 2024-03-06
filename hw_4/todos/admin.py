from django.contrib import admin

from .models import Todo, Todo_list

admin.site.register(Todo)
admin.site.register(Todo_list)
