from django.urls import path
from . import views


app_name = 'blogapp'
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]
