from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class TestMesssageView(TestCase):

	def test_hard(self):
		self.client = Client()
        self.url = reverse('messaging')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('username1', response.content)
        self.assertIn('username2', response.content)
        self.assertIn('username3', response.content)
        self.assertIn('username4', response.content)
        self.assertIn('username5', response.content)
        self.assertIn('username6', response.content)
        self.assertIn('username7', response.content)
        self.assertIn('username8', response.content)
        self.assertIn('username9', response.content)
        self.assertIn('username10', response.content)
