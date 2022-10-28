from django.test import Client, TestCase


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
