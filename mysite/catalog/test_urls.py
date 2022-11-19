from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get(reverse('catalog:list'))
        self.assertEqual(response.status_code, 200)
