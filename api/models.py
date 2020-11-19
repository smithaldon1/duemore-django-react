from django.db import models
from django.utils import timezone

# Inbox Item Model
class InboxItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    convert_to_task = models.BooleanField(null=False, default=False)

# Task Item Model
class TaskItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    start_date_time = models.DateTimeField(default=timezone.now)
    due_date_time = models.DateTimeField()
    duration = models.DurationField()
    is_completed = models.BooleanField(null=False, default=False)

# Project Item Model
class ProjectItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    start_date_time = models.DateTimeField(default=timezone.now)
    due_date_time = models.DateTimeField()
    duration = models.DurationField()


# Filter Item Model


# Timer Item Model


# User Model