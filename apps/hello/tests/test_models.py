import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from apps.hello.models import MyData


class MyDataModelTests(TestCase):

    def test_str(self):
        """ check value that return MyData """
        data = MyData(name='Name')
        self.assertEqual(str(data), u'Name ')

    def test_validate_birthday(self):
        """ check if we can't enter future date """
        test = MyData.objects.create(
            name='Name',
            last_name='LastName1',
            birthday='2010-10-10',
            bio='Bio',
            email='Email@email',
            jabber='J@jabber',
            skype='Skype',
            other_conts='Conts'
        )
        self.client = Client()
        self.url = reverse('contacts')
        response = self.client.get(self.url)
        self.assertIn('2010-10-10', response.content)
