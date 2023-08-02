from http import HTTPStatus
from random import choice, randint

from django.test import TestCase
from django.urls import reverse

from calls.models import Call, Category


class CallSmokeTests(TestCase):
    """
    Tests all views are live in one go
    """

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("calls:call-list")
        cls.template = "calls/call_list.html"

        cls.categories = [
            Category.objects.create(line="I", cost=10),
            Category.objects.create(line="N", cost=2),
            Category.objects.create(line="D", cost=1),
        ]

        cls.calls = [
            Call(duration=randint(1, 100), category=choice(cls.categories))
            for _ in range(3)
        ]

    def test_call_list_view_works(self):
        response = self.client.get(reverse("calls:call-list"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "calls/call_list.html")
        self.assertContains(response, "Calls")
        self.assertNotContains(response, "Hi I should not be on this page")
