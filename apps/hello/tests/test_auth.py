from unittest import TestCase

from django.core.urlresolvers import reverse
from django.test import Client


class TestFormsAjaxAuth(TestCase):
    def test_login_require(self):
        """ Test authentication """
        self.client = Client()
        self.url = reverse('contacts')
        response = self.client.get(reverse('edit_contacts'))
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit_contacts'))
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get(reverse('edit_contacts'))
        self.assertEqual(response.status_code, 302)
