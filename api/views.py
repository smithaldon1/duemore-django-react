from .serializers import InboxSerializer, TaskSerializer, ProjectSerializer, TagSerializer, FilterSerializer
from .models import InboxItem, TaskItem, ProjectItem, TagItem, FilterItem
from rest_framework import generics

class InboxList(generics.ListCreateAPIView):
    queryset = InboxItem.objects.all()
    serializer_class = InboxSerializer

class InboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InboxItem.objects.all()
    serializer_class = InboxSerializer

class TaskList(generics.ListCreateAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskItem.objects.all()
    serializer_class = TaskSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = ProjectItem.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectItem.objects.all()
    serializer_class = ProjectSerializer

class FilterList(generics.ListCreateAPIView):
    queryset = FilterItem.objects.all()
    serializer_class = FilterSerializer

class FilterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FilterItem.objects.all()
    serializer_class = FilterSerializer

class TagList(generics.ListCreateAPIView):
    queryset = TagItem.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TagItem.objects.all()
    serializer_class = TagSerializer