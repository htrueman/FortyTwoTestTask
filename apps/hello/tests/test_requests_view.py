import json
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from django.test import RequestFactory
from apps.hello.models import RequestKeeperModel
from apps.hello.views import requests

class TestRequestKeeperView(TestCase):

    def test_displaying_last_ten_items(self):
        """ check correct displaying last 10 requests"""
        for i in range(5):
            RequestKeeperModel.objects.create(
                name='/test/',
                status=301,
                method='GET'
            )
        for i in range(10):
            RequestKeeperModel.objects.create(
                name='/' + str(i) + '/',
                status=200,
                method='GET'
            )
        response = self.client.get(
            path=reverse('requests'),
            data=dict(last_unread_item=0),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        number_of_requests = len(json.loads(response.content.decode('utf-8')))
        self.assertEqual(number_of_requests, 10)

        requests = RequestKeeperModel.objects.all().order_by('-id')[:10]
        for request in requests:
            self.assertIn(request.name, response.content)
            self.assertIn(request.method, response.content)
            self.assertIn(str(request.status), response.content)

    def test_view_return_right_template(self):
        """ get template returned by view and compare to expected """
        self.factory = RequestFactory()
        request = self.factory.get('/some/url')
        req = requests(request)
        self.assertTemplateUsed(req, 'requests.html')
