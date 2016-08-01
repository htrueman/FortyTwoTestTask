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
        MyData.objects.all().delete()
        test = MyData.objects.create(
            name='Name',
            last_name='LastName',
            birthday=datetime.datetime.now().date(),
            bio='Bio',
            email='Email@email',
            jabber='J@jabber',
            skype='Skype',
            other_conts='Conts'
        )
        self.client = Client()
        self.url = reverse('contacts')
        response = self.client.get(self.url)
        self.assertIn(test.birthday.strftime("%Y-%m-%d"), response.content)
