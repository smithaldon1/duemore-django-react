from api.views import InboxListCreate, ProjectListCreate, TaskListCreate
from django.urls import path
from . import views

urlpatterns = [
    path('api/inbox/', InboxListCreate.as_view()),
    path('api/task/', TaskListCreate.as_view()),
    path('api/project/', ProjectListCreate.as_view()),
]
