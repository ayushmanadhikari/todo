from django.db import models
from django.conf import settings


# models classes
# 1. category class
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category_name


class taskStatus(models.TextChoices):
    not_started = 'not_started'
    in_progress = 'in_progress'
    completed = 'completed'


##main model
class tasks(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.TextField()
    task_category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_status = models.CharField(max_length=20, choices=taskStatus.choices, default=taskStatus.not_started)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
    