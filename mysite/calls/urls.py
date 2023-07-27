from django.urls import path

from calls.views import CallDetailView, CallListView, CallRegisterView, IndexView

app_name = "calls"

urlpatterns = [
    path("", CallListView.as_view(), name="call-list"),
    path("index/", IndexView.as_view(), name="index"),
    path("<uuid:id>/detail/", CallDetailView.as_view(), name="call-detail"),
    path("register/", CallRegisterView.as_view(), name="call-register"),
]
