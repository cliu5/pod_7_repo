from django.db import models

# Create your models here.

# model each item in the todo list


class TodoList(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255)
