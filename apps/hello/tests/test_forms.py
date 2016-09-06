import datetime
from io import BytesIO
from PIL import Image
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from apps.hello.models import MyData


class TestFormsAjaxAuth(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contacts')
        MyData.objects.all().delete()
        MyData.objects.create(
            name='Name',
            last_name='LastName',
            email='Email@mail',
            birthday=datetime.datetime.now().date(),
            skype='Skype',
            bio='Bio',
            other_conts='Conts',
            jabber='Jabber',
        )

    def test_post_form(self):
        """ test form ability to save edited data """
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('edit_contacts'), {
            'name': 'Na',
            'last_name': 'LNa',
            'email': 'em@em.com',
            'skype': 'sc1',
            'jabber': 'jbid@df.com',
            'bio': 'bio1',
            'photo': self.get_photo(),
            'other_conts': 'conts1',
            'birthday': datetime.datetime.now().date()
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('contacts'))
        person = MyData.objects.first()

        self.assertEqual(person.name, 'Na')
        self.assertEqual(person.last_name, 'LNa')
        self.assertEqual(person.email, 'em@em.com')
        self.assertEqual(person.skype, 'sc1')
        self.assertEqual(person.jabber, 'jbid@df.com')
        self.assertEqual(person.bio, 'bio1')
        self.assertEqual(person.other_conts, 'conts1')
        self.assertEqual(person.birthday, datetime.datetime.now().date())
        self.assertTrue(MyData.objects.first().photo)

        self.assertIn(person.name, response.content)
        self.assertIn(person.last_name, response.content)
        self.assertIn(person.email, response.content)
        self.assertIn(person.skype, response.content)
        self.assertIn(person.jabber, response.content)
        self.assertIn(person.bio, response.content)
        self.assertIn(person.other_conts, response.content)

    def test_edit_content(self):
        """ test content on edit page """
        self.client.login(username='admin',
                          password='admin')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Name', response.content)
        self.assertIn('LastName', response.content)
        self.assertIn('Email@mail', response.content)
        self.assertIn('Skype', response.content)
        self.assertIn('Bio', response.content)
        self.assertIn('Conts', response.content)
        self.assertIn('Jabber', response.content)

    def get_photo(self, width=200, height=200):
        """ function that creates photo for next test"""
        photo = BytesIO()
        Image.new('RGBA',
                  (width, height),
                  color=(1, 1, 1)).save(photo, 'JPEG')
        photo.name = 'photo.jpeg'
        photo.seek(0)
        return photo

    def test_photo_resize(self):
        """ test photo resizing """
        self.client.login(username='admin', password='admin')
        self.client.post(reverse('edit_contacts'), {
            'name': 'Na',
            'last_name': 'LNa',
            'email': 'em@em.com2',
            'skype': 'sc2',
            'jabber': 'jbid2@df.com',
            'bio': 'Bio2',
            'photo': self.get_photo(500, 1000),
            'other_conts': 'Conts2',
            'birthday': '2001-11-11'
        }, follow=True)
        tr = MyData.objects.first()
        self.assertEqual(tr.photo.width, 100)
        self.assertEqual(tr.photo.height, 200)

    def test_form_validation(self):
        """ test form ability to save edited data """
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('edit_contacts'), {
            'name': 'Na',
            'last_name': 'LNa',
            'email': 'email',
            'skype': 'sc1',
            'jabber': 'jbid@df.com',
            'bio': 'Bio1',
            'other_conts': 'Conts1',
            'birthday': '2011-11-11'
        }, follow=True)
        self.assertFormError(response, 'form', 'email',
                             [u'Enter a valid email address.'])
