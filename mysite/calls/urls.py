from django.urls import path

from . import views

app_name = 'calls'
urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /calls/list
    path('list/', views.list, name='list'),
    # ex: /calls/register
    path('register/', views.register, name='register'),
         
    ]   