from django.test import TestCase

from apps.hello.models import MyData


class MyDataModelTests(TestCase):
    def test_str(self):
        data = MyData(name='Name')
        self.assertEqual(str(data), u'Name ')