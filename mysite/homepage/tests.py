from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_not_homepage_endpoint(self):
        response = Client().get('/123')
        self.assertEqual(response.status_code, 404)
