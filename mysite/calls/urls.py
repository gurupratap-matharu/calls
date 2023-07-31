from django.urls import path

from calls.views import (
    CallCreateView,
    CallDeleteView,
    CallDetailView,
    CallListView,
    CallUpdateView,
    IndexView,
)

app_name = "calls"

urlpatterns = [
    path("<uuid:pk>/detail/", CallDetailView.as_view(), name="call-detail"),
    path("<uuid:pk>/update/", CallUpdateView.as_view(), name="call-update"),
    path("<uuid:pk>/delete/", CallDeleteView.as_view(), name="call-delete"),
    path("create/", CallCreateView.as_view(), name="call-create"),
    path("index/", IndexView.as_view(), name="index"),
    path("", CallListView.as_view(), name="call-list"),
]
