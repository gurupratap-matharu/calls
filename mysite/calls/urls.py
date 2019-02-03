from django.urls import path

from . import views

app_name = 'calls'
urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name='index'),
    # ex: /calls/list
    path('list/', views.ListView.as_view(), name='list'),
    # ex: /calls/2/detail
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    # ex: /calls/register
    path('register/', views.RegisterView.as_view(), name='register'),

    ]
