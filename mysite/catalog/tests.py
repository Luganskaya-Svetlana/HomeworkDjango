from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    # Все следующие тесты проверяют корректность работы регулярки:

    def test_catalog_normal_num_endpoint(self):
        responses = ['/catalog/123/', '/catalog/12/', '/catalog/1/']
        for response in responses:
            response = Client().get(response)
            self.assertEqual(response.status_code, 200)

    def test_catalog_mixed_endpoint(self):
        response = Client().get('/catalog/1s/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_str_endpoint(self):
        response = Client().get('/catalog/s/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_zero_endpoint(self):
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_start_zero_endpoint(self):
        response = Client().get('/catalog/01/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_negative_num_endpoint(self):
        response = Client().get('/catalog/-1/')
        self.assertEqual(response.status_code, 404)
