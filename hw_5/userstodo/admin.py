from django.contrib import admin

from .models import Todos, User

admin.site.register(Todos)
admin.site.register(User)
