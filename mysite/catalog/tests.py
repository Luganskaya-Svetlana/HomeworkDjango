from django.core.exceptions import ValidationError
from django.test import Client, TestCase

from .models import Category, Item, Tag


class ModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(is_published=True,
                                               name='Тестовая категория',
                                               slug='test-category-slug')
        cls.tag = Tag.objects.create(is_published=True,
                                     name='Тестовый тэг',
                                     slug='test-tag-slug')

    def test_unable_create_without_words(self):
        item_count = Item.objects.count()

        with self.assertRaises(ValidationError):
            create_item(self, 'описание без нужных слов')

        self.assertEqual(Item.objects.count(), item_count)

    def test_able_create_with_words(self):
        must_words = ['роскошно', 'превосходно', 'Роскошно', 'Превосходно',
                      'РОСКОШНО', 'ПРЕВОСХОДНО']
        for word in must_words:
            with self.subTest(word=word):
                item_count = Item.objects.count()
                create_item(self, f'описание с {word}')
                self.assertEqual(Item.objects.count(), item_count + 1)


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)


class RegexTests(TestCase):
    def test_catalog_normal_resp_endpoint(self):
        endpoints = ('/catalog/123/', '/catalog/12/', '/catalog/1/')
        run_tests(self, endpoints, 200)

    def test_catalog_unnormal_resp_endpoint(self):
        endpoints = ('/catalog/0/', '/catalog/01', '/catalog/000/',
                     'catalog/-1/', '/catalog/12s/', '/catalog/s12',
                     '/catalog/0a/', 'catalog/a0/', 'catalog/a0a/',
                     'catalog/1a0/', '/catalog/1-1/', '/catalog/1+1/',
                     '/catalog/1*1/', '/catalog/*s1/', '/catalog/123*1s/',
                     '/catalog/+1/', '/catalog/*1/', '/catalog/1*',
                     '/catalog/s/', '/catalog/s ', '/catalog/-abc/',
                     '/catalog/*/', '/catalog/+/', '/catalog/-/',
                     '/catalog/    /')
        run_tests(self, endpoints, 404)


def run_tests(test, endpoints, expected_status):
    for endpoint in endpoints:
        with test.subTest(endpoint=endpoint):
            response = Client().get(endpoint)
            test.assertEqual(response.status_code, expected_status)


def create_item(test, text):
    test.item = Item(name='Тест',
                     category=test.category,
                     text=text)
    test.item.full_clean()
    test.item.save()
    test.item.tags.add(test.tag)
