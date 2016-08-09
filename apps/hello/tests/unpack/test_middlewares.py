from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.hello.models import RequestKeeperModel


class TestRequestKeeperMiddleware(TestCase):

    def test_middleware_valid_req(self):
        """ check if get correct url """
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
            path=reverse('requests')
        ).count()

        conts_count = RequestKeeperModel.objects.filter(
            path=reverse('contacts')
        ).count()

        get_count = RequestKeeperModel.objects.filter(
            method='GET'
        ).count()

        post_count = RequestKeeperModel.objects.filter(
            method='POST'
        ).count()

        self.assertEqual(post_count, conts_count)
        self.assertEqual(get_count, req_count)

    def test_middleware_invalid_req(self):
        """ check if get wrong url """
        count = RequestKeeperModel.objects.count()

        delta = 3
        for i in xrange(delta):
            self.client.get('/false/url')

        after_count = RequestKeeperModel.objects.count()
        self.assertEqual(
            count + delta, after_count)
