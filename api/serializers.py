from django.db.models import fields
from rest_framework import serializers
from .models import InboxItem, TaskItem, ProjectItem

class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = InboxItem
        fields = ('id', 'name', 'description', 'convert_to_task')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ('id', 'name', 'description', 'start_date_time', 'due_date_time', 'duration', 'is_completed')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItem
        fields = ('id', 'name', 'description', 'start_date_time', 'due_date_time', 'duration')