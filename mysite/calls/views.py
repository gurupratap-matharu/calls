import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View, generic
from django.views.generic import ListView

from .forms import RegisterForm
from .models import Call

logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    """
    CBV for generating simple index view of our calls app.
    User can either chose to
    1. list all the calls in the database
    2. Register a new call in the database
    """

    template_name = "calls/index.html"

    def get_queryset(self):
        return None


class RegisterView(View):
    """
    Our form class that used class based views to render a call register form.
    """

    form_class = RegisterForm
    template_name = "calls/form.html"

    def get(self, request, *args, **kwargs):
        """
        Our inbuilt GET method to render a new blank form
        """
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Our inbuilt POST method to read a saved form or populate it with
        previously filled fields.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            duration = form.cleaned_data["duration"]
            type = form.cleaned_data["type"]

            # create a call in our database
            Call.objects.create(duration=duration, type=type)

            # redirect to a the list all calls url
            return HttpResponseRedirect(reverse("calls:list"))

        return render(request, self.template_name, {"form": form})


class CallListView(ListView):
    """
    List all the calls in the database.
    """

    model = Call
    template_name = "calls/list.html"

    def get_queryset(self):
        qs = super().get_queryset()

        q = self.request.GET.get("q")

        logger.info("q:%s" % q)

        return qs


class DetailView(generic.DetailView):
    """
    Our Detail view class that used django's CBV and shows the detail
    of any particular call in the database.
    """

    model = Call
    template_name = "calls/detail.html"
