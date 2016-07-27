from django.test import TestCase

from apps.hello.models import MyData

class MyDataModelTests(TestCase):
    def test_str(self):
        # check what returns MyData
        data = MyData(name='Name')
        self.assertEqual(str(data), u'Name')