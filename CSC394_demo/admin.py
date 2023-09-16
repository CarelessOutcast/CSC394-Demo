from django.contrib import admin
from .models import user_model, task_model

# Register your models here.
admin.site.register(user_model)
admin.site.register(task_model)