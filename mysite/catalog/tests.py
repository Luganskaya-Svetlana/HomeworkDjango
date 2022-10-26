from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)


class RegexTests(TestCase):
    def test_catalog_normal_resp_endpoint(self):
        run_tests(self, ('/catalog/123/', '/catalog/12/', '/catalog/1/'), 200)

    def test_catalog_unormal_resp_endpoint(self):
        responses = ('/catalog/0/', '/catalog/01', '/catalog/000/',
                     'catalog/-1/', '/catalog/12s/', '/catalog/s12',
                     '/catalog/0a/', 'catalog/a0/', 'catalog/a0a/',
                     'catalog/1a0/', '/catalog/1-1/', '/catalog/1+1/',
                     '/catalog/1*1/', '/catalog/*s1/', '/catalog/123*1s/',
                     '/catalog/+1/', '/catalog/*1/', '/catalog/1*',
                     '/catalog/s/', '/catalog/s ', '/catalog/-abc/',
                     '/catalog/*/', '/catalog/+/', '/catalog/-/',
                     '/catalog/    /')
        run_tests(self, responses, 404)


def run_tests(test, responses, expected_status):
    for resp in responses:
        with test.subTest(resp=resp):
            response = Client().get(resp)
            test.assertEqual(response.status_code, expected_status)
