import logging

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from calls.models import Call

logger = logging.getLogger(__name__)


class IndexView(ListView):
    """
    CBV for generating simple index view of our calls app.
    User can either chose to
    1. list all the calls in the database
    2. Register a new call in the database
    """

    template_name = "calls/index.html"

    def get_queryset(self):
        return None


class CallCreateView(CreateView):
    """
    Register a new call in the app
    """

    model = Call
    fields = ("duration", "category")
    template_name = "calls/call_create_form.html"
    success_url = reverse_lazy("calls:call-list")


class CallListView(ListView):
    """
    List all the calls in the database.
    """

    model = Call
    template_name = "calls/list.html"
    paginate_by = 20

    def get_queryset(self):
        q = self.request.GET.get("q")
        logger.info("q:%s" % q)

        qs = super().get_queryset()
        if q:
            qs = qs.filter(category__line=q)
        return qs


class CallDetailView(DetailView):
    """
    Shows the detail of a single call in the database.
    """

    model = Call
    template_name = "calls/detail.html"


class CallUpdateView(UpdateView):
    model = Call
    fields = ("duration", "category")
    template_name = "calls/call_update_form.html"


class CallDeleteView(DeleteView):
    model = Call
    template_name = "calls/call_confirm_delete.html"
    success_url = reverse_lazy("calls:call-list")
