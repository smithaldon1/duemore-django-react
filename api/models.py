import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Priority Rankings
class Priority(models.TextChoices):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

# Status Rankings
class Status(models.TextChoices):
    NOT_STARTED = 'Not Started'
    UPCOMING = 'Upcoming'
    IN_PROGRESS = 'In Progress'
    DUE_SOON = 'Due Soon'
    OVERDUE = 'Overdue'

# User Model

# Tags Item Model
class TagItem(models.Model):
    tag_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField("Tag Name:", max_length=100)

# Inbox Item Model
class InboxItem(models.Model):
    name = models.CharField("Item Name:", max_length=100)
    description = models.TextField("Item Description:", max_length=300)
    convert_to_task = models.BooleanField("Convert To Task?:", null=False, default=False)
    date_time_created = models.DateTimeField("Date Added:", auto_now_add=True)
    last_modified = models.DateTimeField("Date Modified:", auto_now=True)

# Task Item Model
class SubTaskItem(models.Model):
    subtask_id = models.UUIDField("Task ID:", default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField("Task Name:", max_length=100)
    description = models.TextField("Task Description:", max_length=300)
    tags = models.ManyToManyField(TagItem, related_name='subtask_tags', blank=True)
    task_status = models.CharField("Task Status:", max_length=11, choices=Status.choices, default=Status.IN_PROGRESS)
    start_date_time = models.DateTimeField("Start Date:", default=timezone.now)
    due_date_time = models.DateTimeField("Due Date:")
    duration = models.DurationField("Duration:")
    priority = models.CharField("Task Priority:", max_length=6, choices=Priority.choices, default=Priority.LOW)
    is_completed = models.BooleanField("Is Completed?", null=False, default=False)
    date_time_created = models.DateTimeField("Date Added:", auto_now_add=True)
    last_modified = models.DateTimeField("Date Modified:", auto_now=True)
    
class TaskItem(models.Model):
    task_id = models.UUIDField("Task ID:", default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField("Task Name:", max_length=100)
    description = models.TextField("Task Description:", max_length=300)
    tags = models.ManyToManyField(TagItem, related_name='task_tags', blank=True)
    task_status = models.CharField("Task Status:", max_length=11, choices=Status.choices, default=Status.IN_PROGRESS)
    start_date_time = models.DateTimeField("Start Date:",default=timezone.now)
    due_date_time = models.DateTimeField("Due Date:")
    duration = models.DurationField("Duration:")
    priority = models.CharField("Task Priority:", max_length=6, choices=Priority.choices, default=Priority.LOW)
    is_completed = models.BooleanField("Is Completed?", null=False, default=False)
    child_tasks = models.ManyToManyField(SubTaskItem, related_name='task_child_tasks', blank=True)
    date_time_created = models.DateTimeField("Date Added:", auto_now_add=True)
    last_modified = models.DateTimeField("Date Modified:", auto_now=True)

# Project Item Model
class ProjectItem(models.Model):
    project_id = models.UUIDField("Project ID:", default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField("Project Name:", max_length=100)
    description = models.TextField("Project Description:", max_length=300)
    start_date_time = models.DateTimeField("Start Date:", default=timezone.now)
    due_date_time = models.DateTimeField("Due Date:")
    duration = models.DurationField("Duration:")
    priority = models.CharField("Priority:", max_length=6, choices=Priority.choices, default=Priority.LOW)
    project_status = models.CharField("Project Status:", max_length=11, choices=Status.choices, default=Status.IN_PROGRESS)
    child_tasks = models.ManyToManyField(TaskItem,related_name='project_child_tasks', blank=True)
    date_time_created = models.DateTimeField("Date Added:", auto_now_add=True)
    last_modified = models.DateTimeField("Date Modified:", auto_now=True)

# Filter Item Model
class FilterItem(models.Model):
    filter_id = models.UUIDField("Filter ID:", default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField("Filter Name:", max_length=100)
    date_time_created = models.DateTimeField("Date Added:", auto_now_add=True)

# Timer Item Model
