from django.test import TestCase
from apps.hello.models import MyData, RequestKeeperModel


class MyDataModelTests(TestCase):

    def test_str(self):
        """ check value that return MyData """
        data = MyData(name='Name')
        self.assertEqual(str(data), u'Name ')


class RequestKeeperModelTests(TestCase):

    def test_str(self):
        """ check value that return requests """
        info = RequestKeeperModel(name='/')
        self.assertEqual(str(info), u'/')
