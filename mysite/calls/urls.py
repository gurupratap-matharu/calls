from django.urls import path

from calls.views import CallListView, DetailView, IndexView, RegisterView

app_name = "calls"

urlpatterns = [
    path("", CallListView.as_view(), name="list"),
    path("index/", IndexView.as_view(), name="index"),
    path("<uuid:pk>/detail/", DetailView.as_view(), name="detail"),
    path("register/", RegisterView.as_view(), name="register"),
]
