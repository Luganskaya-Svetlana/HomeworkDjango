from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)


class HomePageTests(TestCase):
    fixtures = ['data_for_tests.json']

    def test_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)

    def test_correct_len_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(len(response.context['items']), 2)

    def test_correct_sort_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(response.context['items'][0].id, 5)
        self.assertEqual(response.context['items'][1].id, 1)
