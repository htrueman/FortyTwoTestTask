from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.hello.models import RequestKeeperModel


class TestRequestKeeperMiddleware(TestCase):

    def test_reqs_storing(self):
        """
        check if get get several, also check counts
        for POST and GET request type to make sure
        it stores right
        """
        count = RequestKeeperModel.objects.count()

        delta_post = 3
        for i in xrange(delta_post):
            self.client.post(reverse('contacts'))

        delta_get = 4
        for i in xrange(delta_get):
            self.client.get(reverse('requests'))

        after_count = RequestKeeperModel.objects.count()
        self.assertEqual(
            count + delta_post + delta_get, after_count)

        req_count = RequestKeeperModel.objects.filter(
            name=reverse('requests')
        ).count()

        conts_count = RequestKeeperModel.objects.filter(
            name=reverse('contacts')
        ).count()

        get_count = RequestKeeperModel.objects.filter(
            method='GET'
        ).count()

        post_count = RequestKeeperModel.objects.filter(
            method='POST'
        ).count()

        self.assertEqual(post_count, conts_count)
        self.assertEqual(get_count, req_count)

    def test_with_static_req(self):
        " make static request to ensure it does't present on template "
        RequestKeeperModel.objects.all().delete()
        self.client.logout()
        self.url = reverse('requests')
        self.client.get('/static/some_req')
        response = self.client.get(self.url)
        self.assertNotIn('/static/some_req', response.content)

    def test_anon_user(self):
        """ check if request is from anonymous user,
        requests.html page should display anonymous
        as author of request """
        RequestKeeperModel.objects.all().delete()
        self.client.logout()
        self.url = reverse('requests')
        self.client.get('/some/url')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('anonymous', response.content)

    def test_auth_user(self):
        """ check if request is from authenticated user,
        requests.html page should display username
        as author of request """
        RequestKeeperModel.objects.all().delete()
        self.client.login(username='admin', password='admin')
        self.client.get('/some/url')
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('admin', response.content)
