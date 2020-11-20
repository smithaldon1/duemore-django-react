from .serializers import InboxSerializer, TaskSerializer, ProjectSerializer, TagSerializer, FilterSerializer
from .models import InboxItem, TaskItem, ProjectItem, TagItem, FilterItem
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

class FilterListCreate(generics.ListCreateAPIView):
    queryset = FilterItem.objects.all()
    serializer_class = FilterSerializer

class TagListCreate(generics.ListCreateAPIView):
    queryset = TagItem.objects.all()
    serializer_class = TagSerializer