from django.test import TestCase, RequestFactory
from calc import views


class ExampleViewTestCase(TestCase):

    def test_add(self):
        print("Running Test Cases For Add")
        status_code = 200
        view = views.add
        
        req = RequestFactory().get('/add')

        data = [[3, 4], [5, 6], [9, 12]]
        result = [7, 11, 21]

        for d, r in zip(data, result):
            resp = views.add(req, *d)
            self.assertEqual(int(resp.content), r)