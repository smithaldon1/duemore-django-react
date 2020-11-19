from .serializers import InboxSerializer, TaskSerializer, ProjectSerializer
from .models import InboxItem, TaskItem, ProjectItem
from rest_framework import generics

class InboxListCreate(generics.ListCreateAPIView):
    queryset = InboxItem.objects.all()
    serializer_class = InboxSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskSerializer

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = ProjectItem.objects.all()
    serializer_class = ProjectSerializer