from django.urls import path

from . import views

app_name = "calls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("list/", views.ListView.as_view(), name="list"),
    path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
    path("register/", views.RegisterView.as_view(), name="register"),
]
