from django.test import TestCase

from .models import Call, Type


class CallModelTests(TestCase):
    def test_domestic_call_returns_fixed_cost(self):
        """irrespective of duration fixed value should be returned"""

        domestic = Type(type="Domestic", cost=100)
        domestic.save()
        c1 = Call(duration=10, type=domestic)
        c2 = Call(duration=500, type=domestic)
        c3 = Call(duration=8000, type=domestic)
        c4 = Call(duration=90000, type=domestic)
        c5 = Call(duration=100000, type=domestic)
        c6 = Call(duration=9999999999, type=domestic)

        c1.save()
        c2.save()
        c3.save()
        c4.save()
        c5.save()
        c6.save()

        self.assertIs(c1.cost, domestic.cost)
        self.assertIs(c2.cost, domestic.cost)
        self.assertIs(c3.cost, domestic.cost)
        self.assertIs(c4.cost, domestic.cost)
        self.assertIs(c5.cost, domestic.cost)
        self.assertIs(c6.cost, domestic.cost)

    def test_domestic_call_with_negative_or_zero_duration(self):
        """negative or zero duration should return zero cost"""

        domestic = Type(type="Domestic", cost=100)
        domestic.save()
        c1 = Call(duration=-10, type=domestic)
        c2 = Call(duration=-500, type=domestic)
        c3 = Call(duration=-8000, type=domestic)
        c4 = Call(duration=-90000, type=domestic)
        c5 = Call(duration=-100000, type=domestic)
        c6 = Call(duration=-9999999999, type=domestic)
        c7 = Call(duration=0, type=domestic)

        c1.save()
        c2.save()
        c3.save()
        c4.save()
        c5.save()
        c6.save()
        c7.save()

        self.assertIs(c1.cost, 0)
        self.assertIs(c2.cost, 0)
        self.assertIs(c3.cost, 0)
        self.assertIs(c4.cost, 0)
        self.assertIs(c5.cost, 0)
        self.assertIs(c6.cost, 0)
        self.assertIs(c7.cost, 0)

    def test_national_call_return_correct_cost(self):
        """for positive duration correct cost should be returned"""

        national = Type(type="national", cost=0.01)
        national.save()
        c1 = Call(duration=10, type=national)
        c2 = Call(duration=500, type=national)
        c3 = Call(duration=8000, type=national)
        c4 = Call(duration=90000, type=national)
        c5 = Call(duration=100000, type=national)
        c6 = Call(duration=9999999999, type=national)

        c1.save()
        c2.save()
        c3.save()
        c4.save()
        c5.save()
        c6.save()

        self.assertEqual(c1.cost, 0.1)
        self.assertEqual(c2.cost, 5)
        self.assertEqual(c3.cost, 80)
        self.assertEqual(c4.cost, 900)
        self.assertEqual(c5.cost, 1000)
        self.assertEqual(c6.cost, 99999999.99)

    def test_national_call_with_negative_or_zero_duration(self):
        """for negative or zero duration zero cost should be returned"""

        national = Type(type="national", cost=0.01)
        national.save()
        c1 = Call(duration=-10, type=national)
        c2 = Call(duration=-500, type=national)
        c3 = Call(duration=-8000, type=national)
        c4 = Call(duration=-90000, type=national)
        c5 = Call(duration=-100000, type=national)
        c6 = Call(duration=-9999999999, type=national)
        c7 = Call(duration=0, type=national)

        c1.save()
        c2.save()
        c3.save()
        c4.save()
        c5.save()
        c6.save()
        c7.save()

        self.assertEqual(c1.cost, 0)
        self.assertEqual(c2.cost, 0)
        self.assertEqual(c3.cost, 0)
        self.assertEqual(c4.cost, 0)
        self.assertEqual(c5.cost, 0)
        self.assertEqual(c6.cost, 0)
        self.assertEqual(c7.cost, 0)

    def test_international_call_returns_correct_cost(self):
        """for positive duration correct cost should be returned"""

        international = Type(type="international", cost=1)
        international.save()
        c1 = Call(duration=10, type=international)
        c2 = Call(duration=500, type=international)
        c3 = Call(duration=8000, type=international)
        c4 = Call(duration=90000, type=international)
        c5 = Call(duration=100000, type=international)
        c6 = Call(duration=9999999999, type=international)

        c1.save()
        c2.save()
        c3.save()
        c4.save()
        c5.save()
        c6.save()

        self.assertEqual(c1.cost, 10)
        self.assertEqual(c2.cost, 500)
        self.assertEqual(c3.cost, 8000)
        self.assertEqual(c4.cost, 90000)
        self.assertEqual(c5.cost, 100000)
        self.assertEqual(c6.cost, 9999999999)

    def test_international_call_with_negative_or_zero_duration(self):
        """for negative or zero duration zero cost should be returned"""

        international = Type(type="international", cost=1)
        international.save()
        c1 = Call(duration=-10, type=international)
        c2 = Call(duration=-500, type=international)
        c3 = Call(duration=-8000, type=international)
        c4 = Call(duration=-90000, type=international)
        c5 = Call(duration=-100000, type=international)
        c6 = Call(duration=-9999999999, type=international)
        c7 = Call(duration=0, type=international)

        c1.save()
        c2.save()
        c3.save()
        c4.save()
        c5.save()
        c6.save()
        c7.save()

        self.assertEqual(c1.cost, 0)
        self.assertEqual(c2.cost, 0)
        self.assertEqual(c3.cost, 0)
        self.assertEqual(c4.cost, 0)
        self.assertEqual(c5.cost, 0)
        self.assertEqual(c6.cost, 0)
        self.assertEqual(c7.cost, 0)
