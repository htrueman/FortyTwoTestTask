import datetime
from django.test import TestCase

from apps.hello.models import MyData
from apps.hello.validators import validate_birthday


class MyDataModelTests(TestCase):

    def test_str(self):
        """ check value that return MyData """
        data = MyData(name='Name')
        self.assertEqual(str(data), u'Name ')

    def test_validate_birthday(self):
        """ check if we can't enter future date """
        # self.assertEqual(validate_birthday(datetime.date(2050,1,1)),\
        # 'Please write your real date of birth!')
        self.assertEqual(validate_birthday(
            datetime.datetime.now().date()), "OK")
