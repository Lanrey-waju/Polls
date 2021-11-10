from django.urls import path
from . import views


app_name = 'polls'
# Define your urlpatterns here
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:question_id>/', views.question_detail, name='detail')
]