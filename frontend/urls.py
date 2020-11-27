from django.conf.urls import url
from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    url(r'^(?:.*)/?$', index),
]
