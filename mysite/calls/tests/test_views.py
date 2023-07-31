from random import choice, randint

from django.test import TestCase
from django.urls import resolve, reverse

from calls.models import Call, Category
from calls.views import CallListView


class CallListViewTests(TestCase):
    """
    Tests suite for the call list view
    """

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("calls:call-list")
        cls.template = "calls/call_list.html"

        category_objs = [Category("I", 10), Category("N", 2), Category("D", 1)]
        cls.categories = Category.objects.bulk_create(objs=category_objs)

        call_objs = [
            Call(duration=randint(1, 100), category=choice(category_objs))
            for _ in range(3)
        ]
        cls.calls = Call.objects.bulk_create(objs=call_objs)

    def test_call_list_url_resolves_correct_view(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, CallListView.as_view().__name__)
