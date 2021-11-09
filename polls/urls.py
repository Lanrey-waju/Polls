from django.urls import path
from . import views


# Define your urlpatterns here
urlpatterns = [
  path('', views.index, name='index')
]