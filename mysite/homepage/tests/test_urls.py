from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.status_code, 200)
