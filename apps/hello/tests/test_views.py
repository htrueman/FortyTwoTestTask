import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from apps.hello.models import MyData


class TestContactData(TestCase):

    def setUp(self):
        MyData.objects.all().delete()
        MyData.objects.get_or_create(
            name='Name1',
            last_name='LastName1',
            birthday='2001-01-01',
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
            birthday='2002-02-02',
            bio='Bio2',
            email='Email@email2',
            jabber='J@jabber2',
            skype='Skype2',
            other_conts='Conts2'
        )
        MyData.objects.get_or_create(
            name='Name3',
            last_name='LastName3',
            birthday='2003-03-03',
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

    def test_birthday(self):
        """ test if date of birth from the future """
        MyData.objects.all().delete()
        MyData.objects.get_or_create(
            birthday=datetime.date(2020, 1, 1)
            )
        self.client = Client()
        self.url = reverse('contacts')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Please write your real date of birth!", response.content)


class TestRequestsData(TestCase):
    """check requests_data view"""
    def test_requests_data(self):
        """check if hardcoded requests_data returns 10 last requests"""
        requests = [
            'GET /requests/ 200',
            'GET /edit/add/ 200',
            'GET /img/upload/img1.png 304',
            'GET /img/upload/img2.png 404',
            'GET /requests/ 200',
            'GET / 200',
            'GET /requests/ 200',
            'GET / 200',
            'GET /requests/ 200',
            'GET /edit/ 200',
            'GET /requests/ 200',
            'GET /requests/ 200',
            'GET /requests/ 200',
            'GET /requests/ 200',
            'GET /requests/ 200',
            'GET /requests/ 200']
        self.client = Client()
        self.url = reverse('requests')
        response = self.client.get(self.url)

        self.assertEqual(len(response.context['requests']), 10)