from django.test import Client, TestCase
from django.urls import reverse


class ItemListPageTests(TestCase):
    fixtures = ['data_for_tests.json']

    def test_correct_context(self):
        response = Client().get(reverse('catalog:list'))
        self.assertIn('items', response.context)

    def test_correct_len_context(self):
        response = Client().get(reverse('catalog:list'))
        self.assertEqual(len(response.context['items']), 5)

    def test_correct_sort_context(self):
        response = Client().get(reverse('catalog:list'))
        self.assertEqual(response.context['items'][0].id, 2)
        self.assertEqual(response.context['items'][4].id, 4)


class ItemDetailPageTests(TestCase):
    fixtures = ['data_for_tests.json']

    def test_not_found(self):
        self.run_tests(['/catalog/6/', '/catalog/123/', '/catalog/1000/'], 404)
        # в запросах id скрытых или несуществующих товаров

    def test_items_found(self):
        self.run_tests(['/catalog/1/', '/catalog/2/', '/catalog/3/',
                        '/catalog/4/', '/catalog/5/'], 200)

    def run_tests(self, endpoints, status_code):
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                response = Client().get(endpoint)
                self.assertEqual(response.status_code, status_code)

    def test_correct_context(self):
        endpoints = ['/catalog/1/', '/catalog/2/', '/catalog/3/',
                     '/catalog/4/', '/catalog/5/']
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                response = Client().get(endpoint)
                self.assertIn('item', response.context)
