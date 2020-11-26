from django.db.models import fields
from rest_framework import serializers
from .models import FilterItem, TagItem, InboxItem, SubTaskItem, TaskItem, ProjectItem

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagItem
        fields = (
            'id',
            'tag_id',
            'name'
        )

class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = InboxItem
        fields = (
            'id',
            'name',
            'description',
            'convert_to_task',
            'date_time_created',
            'last_modified'
        )

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTaskItem
        fields = (
            'id',
            'subtask_id',
            'name',
            'description',
            'tags',
            'task_status',
            'start_date_time',
            'due_date_time',
            'duration',
            'priority',
            'is_completed',
            'date_time_created',
            'last_modified'
        )

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = (
            'id', 
            'task_id', 
            'name', 
            'description', 
            'tags', 
            'task_status', 
            'start_date_time', 
            'due_date_time', 
            'duration', 
            'priority', 
            'is_completed', 
            'child_tasks', 
            'date_time_created', 
            'last_modified'
        )

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItem
        fields = (
            'id', 
            'project_id', 
            'name', 
            'description', 
            'start_date_time', 
            'due_date_time', 
            'duration', 
            'priority', 
            'project_status', 
            'child_tasks', 
            'date_time_created', 
            'last_modified'
        )

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterItem
        fields = (
            'id', 
            'filter_id',
            'name',
            'date_time_created'
        )