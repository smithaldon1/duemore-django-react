from django.urls import path
from . import views


urlpatterns = [
    path('inbox/', views.InboxList.as_view()),
    path('inbox/<int:pk>', views.InboxDetail.as_view()),
    path('task/', views.TaskList.as_view()),
    path('task/<int:pk>', views.TaskDetail.as_view()),
    path('project/', views.ProjectList.as_view()),
    path('project/<int:pk>', views.ProjectDetail.as_view()),
    path('filter/', views.FilterList.as_view()),
    path('filter/<int:pk>', views.FilterDetail.as_view()),
    path('tag/', views.TagList.as_view()),
    path('tag/<int:pk>', views.TagDetail.as_view())
]
