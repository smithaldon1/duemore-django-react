from api.views import InboxListCreate, ProjectListCreate, TaskListCreate, TagListCreate, FilterListCreate
from django.urls import path

urlpatterns = [
    path('api/inbox/', InboxListCreate.as_view()),
    path('api/task/', TaskListCreate.as_view()),
    path('api/project/', ProjectListCreate.as_view()),
    path('api/filter/', FilterListCreate.as_view()),
    path('api/tag/', TagListCreate.as_view())
]
