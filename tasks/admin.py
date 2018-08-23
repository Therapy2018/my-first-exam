from django.contrib import admin

from .models import Task

admin.site.register(Task)

from .models import Answer

admin.site.register(Answer)
