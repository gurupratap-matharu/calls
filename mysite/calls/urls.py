from django.urls import path

from calls.views import CallCreateView, CallDetailView, CallListView, IndexView

app_name = "calls"

urlpatterns = [
    path("", CallListView.as_view(), name="call-list"),
    path("index/", IndexView.as_view(), name="index"),
    path("<uuid:pk>/detail/", CallDetailView.as_view(), name="call-detail"),
    path("create/", CallCreateView.as_view(), name="call-create"),
]
