import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.hello.models import MyData


class MyDataModelTests(TestCase):
    def setUp(self):
        MyData.objects.all().delete()
        MyData.objects.create(
                name='Name1',
                last_name='LastName',
                birthday=datetime.date(2020, 1, 1),
                bio='Bio',
                email='Email@email.ua',
                jabber='J@jabber.ua',
                skype='Skype',
                other_conts='Conts'
            )

    def test_validate_name_last_name(self):
        """ check if we can only pass alphabetic
        characters in name/last_name field """
        test = MyData.objects.first()
        with self.assertRaisesMessage(
                ValidationError,
                'This field should contain '
                'alphabetic characters only'):
            test.clean_fields()

    def test_birthday(self):
        """check if we can't enter future date in birtday field """
        test = MyData.objects.first()
        with self.assertRaisesMessage(
                ValidationError,
                'Please, write your real date of birth!'):
            test.clean_fields()
