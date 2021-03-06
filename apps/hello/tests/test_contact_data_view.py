import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from apps.hello.models import MyData


class TestContactData(TestCase):

    def setUp(self):
        MyData.objects.all().delete()
        MyData.objects.create(
            name='Name1',
            last_name='LastName1',
            birthday=datetime.datetime.now().date(),
            bio='Bio1',
            email='Email@email1',
            jabber='J@jabber1',
            skype='Skype1',
            other_conts='Conts1'
        )

    def test_one(self):
        """ test if one odject in database """
        self.client = Client()
        self.url = reverse('contacts')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Name1', response.content)
        self.assertIn('LastName1', response.content)
        self.assertIn('Bio1', response.content)
        self.assertIn('Email@email1', response.content)
        self.assertIn('J@jabber1', response.content)
        self.assertIn('Skype1', response.content)
        self.assertIn('Conts1', response.content)

    def test_many(self):
        """ test if more than one object in database """
        MyData.objects.all().delete()
        MyData.objects.get_or_create(
            name='Name2',
            last_name='LastName2',
            birthday=datetime.datetime.now().date(),
            bio='Bio2',
            email='Email@email2',
            jabber='J@jabber2',
            skype='Skype2',
            other_conts='Conts2'
        )
        MyData.objects.get_or_create(
            name='Name3',
            last_name='LastName3',
            birthday=datetime.datetime.now().date(),
            bio='Bio3',
            email='Email@email3',
            jabber='J@jabber3',
            skype='Skype3',
            other_conts='Conts3'
        )

        self.client = Client()
        self.url = reverse('contacts')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('Name2', response.content)
        self.assertIn('LastName2', response.content)
        self.assertIn('Bio2', response.content)
        self.assertIn('Email@email2', response.content)
        self.assertIn('J@jabber2', response.content)
        self.assertIn('Skype2', response.content)
        self.assertIn('Conts2', response.content)

    def test_none(self):
        """ test if there are no objects in database """
        MyData.objects.all().delete()
        self.client = Client()
        self.url = reverse('contacts')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("There are no objects in database", response.content)
