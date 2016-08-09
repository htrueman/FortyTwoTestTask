import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
import traceback

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
                name='Name',
                last_name='LastName',
                birthday=datetime.date(2020, 1, 1),
                bio='Bio',
                email='Email@email.ua',
                jabber='J@jabber.ua',
                skype='Skype',
                other_conts='Conts'
            )
        try:
            test.clean_fields()
        except ValidationError:
            self.assertIn("ValidationError", traceback.format_exc())


class RequestKeeperModelTests(TestCase):

    def test_create_fields(self):
        """ check if model's fields created successfully """
        test_req = RequestKeeperModel.objects.create(
                path='path',
                method='method',
                date=datetime.date(2016, 1, 1),
                is_viewed=True
            )
        test_req.clean_fields()
