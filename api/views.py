from .serializers import InboxSerializer, TaskSerializer, ProjectSerializer, TagSerializer, FilterSerializer
from .models import InboxItem, TaskItem, ProjectItem, TagItem, FilterItem
from rest_framework import generics
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter

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