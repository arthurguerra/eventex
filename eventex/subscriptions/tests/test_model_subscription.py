from django.test import TestCase
from django.shortcuts import resolve_url as r
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Arthur Guerra',
            cpf='12345678901',
            email='arthurjguerra@gmail.com',
            phone='73-98833-8187'
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Arthur Guerra', str(self.obj))

    def test_paid_default_false(self):
        """By default, paid must be false"""
        self.assertEqual(False, self.obj.paid)

    def test_get_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())

