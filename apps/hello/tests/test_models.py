from django.test import TestCase

from apps.hello.models import MyData, RequestKeeperModel


class MyDataModelTests(TestCase):

    def test_str(self):
        """ check value that return MyData """
        data = MyData(name='Name')
        self.assertEqual(str(data), u'Name ')


class RequestKeeperModelTests(TestCase):

    def test_unicode(self):
        """ check value that return MyData """
        request = RequestKeeperModel(name='Name')
        self.assertEqual(unicode(request), u'Name')
