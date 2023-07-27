import logging

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import Call

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


class CallRegisterView(CreateView):
    """
    Register a new call in the app
    """

    model = Call
    fields = ("duration", "category")
    template_name = "calls/form.html"
    success_url = reverse_lazy("calls:call-list")


class CallListView(ListView):
    """
    List all the calls in the database.
    """

    model = Call
    template_name = "calls/list.html"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()

        q = self.request.GET.get("q")

        logger.info("q:%s" % q)

        return qs


class CallDetailView(DetailView):
    """
    Our Detail view class that used django's CBV and shows the detail
    of any particular call in the database.
    """

    model = Call
    pk_url_kwarg = "id"
    template_name = "calls/detail.html"
