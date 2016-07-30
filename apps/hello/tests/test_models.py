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
        test = MyData.objects.create(
            name='Name',
            last_name='LastName1',
            birthday=datetime.date(2010,1,1),
            bio='Bio',
            email='Email@email',
            jabber='J@jabber',
            skype='Skype',
            other_conts='Conts'
        )
        self.assertEqual(validate_birthday(
            test.birthday), "Done")
