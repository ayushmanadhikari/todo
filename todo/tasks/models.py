from django.contrib.auth.models import User
from django.db import models


# models classes
# 1. category class
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cattegory_name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('user', 'cattegory_name')
    
    def __str__(self):
        return self.cattegory_name


class taskStatus(models.TextChoices):
    not_started = 'not_started'
    in_progress = 'in_progress'
    completed = 'completed'



##main model
class tasks(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    task_category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    task_status = models.CharField(max_length=20, choices=taskStatus.choices, default=taskStatus.not_started)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
    