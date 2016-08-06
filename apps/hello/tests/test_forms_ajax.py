import datetime
from io import BytesIO
from PIL import Image
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from apps.hello.models import MyData


class TestFormsAjax(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contacts')
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

    def test_edit_content(self):
        """ Test content on edit page """
        self.client.login(username='admin',
                          password='admin')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Name1', response.content)
        self.assertIn('LastName1', response.content)
        self.assertIn('Bio1', response.content)
        self.assertIn('Email@email1', response.content)
        self.assertIn('J@jabber1', response.content)
        self.assertIn('Skype1', response.content)
        self.assertIn('Conts1', response.content)

    def get_photo(self, width=200, height=200):
        """ function that create photo for next test"""
        photo = BytesIO()
        Image.new(
            'RGBA',
            (width, height),
            color=(1, 1, 1)).save(photo, 'JPEG')
        photo.name = 'photo.jpeg'
        photo.seek(0)
        return photo

    def test_post_form(self):
        """ test for form ability save edited data"""
        self.client.login(
            username='admin',
            password='admin')
        response = self.client.post(reverse('edit_contacts'), {
            'name': 'Name1',
            'last_name': 'LastName1',
            'email': 'Bio1',
            'skype': 'Email@email1',
            'jabber': 'J@jabber1',
            'bio': 'Skype1',
            'photo': self.get_photo(),
            'other_conts': 'Conts1',
            'birthday': datetime.datetime.now().date()
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('contacts'))
        person = MyData.objects.first()

        self.assertEqual(person.name, 'N1')
        self.assertEqual(person.last_name, 'LN2')
        self.assertEqual(person.email, 'em@em.com')
        self.assertEqual(person.skype, 'sc1')
        self.assertEqual(person.jabber, 'jbid@df.com')
        self.assertEqual(person.bio, 'sdsdsdsd')
        self.assertEqual(person.other_contacts, 'cxcxcx')
        self.assertEqual(person.date_of_birth, date(2011, 11, 11))
        self.assertTrue(MyData.objects.first().photo)

        self.assertIn(person.name, response.content)
        self.assertIn(person.last_name, response.content)
        self.assertIn(person.email, response.content)
        self.assertIn(person.skype, response.content)
        self.assertIn(person.jabber, response.content)
        self.assertIn(person.bio, response.content)
        self.assertIn(person.other_contacts, response.content)

    def test_photo_resize(self):
        """Test photo resize"""
        self.client.login(
            username='admin',
            password='admin')
        self.client.post(reverse('edit_contacts'), {
            'name': 'N11',
            'last_name': 'LN22',
            'email': 'em@em.com1',
            'skype': 'sc11',
            'jabber': 'jbid1@df.com',
            'bio': 'sdsdsdsd',
            'photo': self.get_photo(500, 1000),
            'other_contacts': 'cxc1xcx',
            'date_of_birth': '2001-11-11'
        }, follow=True)
        tr = MyData.objects.first()
        self.assertEqual(tr.photo.width, 100)
        self.assertEqual(tr.photo.height, 200)

    def test_form_validation(self):
        """ test for form ability save edited data"""
        self.client.login(
            username='admin',
            password='admin')
        response = self.client.post(reverse('edit_contacts'), {
            'name': 'N1',
            'last_name': 'LN2',
            'email': 'email',
            'skype': 'sc1',
            'jabber': 'jbid@df.com',
            'bio': 'sdsdsdsd',
            'other_contacts': 'cxcxcx',
            'date_of_birth': '2011-11-11'
        }, follow=True)
        self.assertFormError(response, 'form', 'email',
                             [u'Enter a valid email address.'])
