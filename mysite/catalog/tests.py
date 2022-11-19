from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from .models import Category, Item, Tag


class ModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(name='Тестовая категория',
                                               slug='test-category-slug')
        cls.tag = Tag.objects.create(name='Тестовый тэг',
                                     slug='test-tag-slug')

    def test_unable_create_without_words(self):
        wrong_words = ['', 'нероскошно', 'йлцорудыфвпревосходнойцуйцлур']
        for word in wrong_words:
            with self.subTest(word=word):
                item_count = Item.objects.count()
                with self.assertRaises(ValidationError):
                    self.create_item(f'описание без нужных слов, но с {word}')
                self.assertEqual(Item.objects.count(), item_count)

    def test_able_create_with_words(self):
        must_words = ['роскошно', 'превосходно', 'Роскошно', 'Превосходно',
                      'РОСКОШНО', 'ПРЕВОСХОДНО', 'превосходно!',
                      'превосходно?', 'роскошно,', 'роскошно.',
                      'превосходно,роскошно', 'Супер (роскошно)']
        for word in must_words:
            with self.subTest(word=word):
                item_count = Item.objects.count()
                self.create_item(f'описание с {word}')
                self.assertEqual(Item.objects.count(), item_count + 1)

    def create_item(self, text):
        self.item = Item(name='Тест',
                         category=self.category,
                         text=text)
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)


class RegexTests(TestCase):
    fixtures = ["data_for_tests.json"]

    def test_catalog_normal_resp_endpoint(self):
        endpoints = ('/catalog/3/', '/catalog/2/', '/catalog/1/')
        self.run_tests(endpoints, 200)

    def test_catalog_unnormal_resp_endpoint(self):
        endpoints = ('/catalog/0/', '/catalog/01/', '/catalog/000/',
                     'catalog/-1/', '/catalog/12s/', '/catalog/s12',
                     '/catalog/0a/', 'catalog/a0/', 'catalog/a0a/',
                     'catalog/1a0/', '/catalog/1-1/', '/catalog/1+1/',
                     '/catalog/1*1/', '/catalog/*s1/', '/catalog/123*1s/',
                     '/catalog/+1/', '/catalog/*1/', '/catalog/1*',
                     '/catalog/s/', '/catalog/s ', '/catalog/-abc/',
                     '/catalog/*/', '/catalog/+/', '/catalog/-/',
                     '/catalog/    /')
        self.run_tests(endpoints, 404)

    def run_tests(self, endpoints, expected_status):
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                response = Client().get(endpoint)
                self.assertEqual(response.status_code, expected_status)


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
