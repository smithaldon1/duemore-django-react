from api.views import InboxListCreate, ProjectListCreate, TaskListCreate, TagListCreate, FilterListCreate, FacebookLogin, GoogleLogin, GithubLogin
from django.urls import path

urlpatterns = [
    path('api/inbox/', InboxListCreate.as_view()),
    path('api/task/', TaskListCreate.as_view()),
    path('api/project/', ProjectListCreate.as_view()),
    path('api/filter/', FilterListCreate.as_view()),
    path('api/tag/', TagListCreate.as_view()),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('rest-auth/github/', GithubLogin.as_view(), name='github_login')
]
