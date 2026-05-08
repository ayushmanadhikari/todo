from django.contrib import admin
from .models import tasks, Category
# Register your models here.

admin.site.register(tasks)
admin.site.register(Category)
