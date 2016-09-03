import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.hello.models import MyData, RequestKeeperModel


class MyDataModelTests(TestCase):

    def test_str(self):
        """ check value that return MyData """
        data = MyData(name='Name')
        self.assertEqual(str(data), u'Name ')

    def test_validate_birthday(self):
        """ check if we can't enter future date """
        MyData.objects.all().delete()
        test = MyData.objects.create(
                name='Name1',
                last_name='LastName',
                birthday=datetime.date(2020, 1, 1),
                bio='Bio',
                email='Email@email.ua',
                jabber='J@jabber.ua',
                skype='Skype',
                other_conts='Conts'
            )
        with self.assertRaisesMessage(
                                    ValidationError,
                                    'This field should contain '
                                    'alphabetic characters only'):
            test.clean_fields()
        with self.assertRaisesMessage(
                                    ValidationError,
                                    'Please, write your real date of birth!'):
            test.clean_fields()


class RequestKeeperModelTests(TestCase):

    def test_str(self):
        """ check value that return requests """
        info = RequestKeeperModel(name='/')
        self.assertEqual(str(info), u'/')
