from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)


class RegexTests(TestCase):
    def test_catalog_normal_num_endpoint(self):
        responses = ['/catalog/123/', '/catalog/12/', '/catalog/1/']
        for resp in responses:
            with self.subTest(resp=resp):
                response = Client().get(resp)
                self.assertEqual(response.status_code, 200)

    def test_unormal_num_endpoint(self):
        responses = ['/catalog/0/', '/catalog/01', '/catalog/000/',
                     'catalog/-1/']
        for resp in responses:
            with self.subTest(resp=resp):
                response = Client().get(resp)
                self.assertEqual(response.status_code, 404)

    def test_catalog_mixed_endpoint(self):
        responses = ['/catalog/12s/', '/catalog/s12', '/catalog/0a/',
                     'catalog/a0/', 'catalog/a0a/', 'catalog/1a0/',
                     '/catalog/1\n/', '/catalog/\n1/', '/catalog/1\n1/',
                     '/catalog/s\n1/', '/catalog/123\n1/', '/catalog/\t1/',
                     '/catalog/1\t/', '/catalog/1 ']
        for resp in responses:
            with self.subTest(resp=resp):
                response = Client().get(resp)
                self.assertEqual(response.status_code, 404)

    def test_catalog_str_endpoint(self):
        responses = ['/catalog/s/', '/catalog/s\n', '/catalog/\n/',
                     '/catalog/a0/', '/catalog/a0a/', '/catalog/1a0/',
                     '/catalog/\t/', '/catalog/\tsv/', '/catalog/sv\t/',
                     '/catalog/\n\t/', '/catalog/    /']
        for resp in responses:
            with self.subTest(resp=resp):
                response = Client().get(resp)
                self.assertEqual(response.status_code, 404)
