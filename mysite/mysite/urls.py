from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # django administration
    path("dj-admin/", admin.site.urls),
    # Local apps
    path("calls/", include("calls.urls")),
]
