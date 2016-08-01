
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import RequestFactory

from apps.hello.views import RequestKeeperView


class TestRequestKeeperView(TestCase):

    def test_req_template(self):
        """ check if there is expected template """
        request = RequestFactory().get(reverse('requests'))
        view_function = RequestKeeperView.as_view()
        result = view_function(request)
        self.assertTemplateUsed(result, 'requests.html')

    def test_fetching_from_db(self):
        """ check if aster false reqs new correct req will pas """
        for i in xrange(10):
            self.client.put("/false/url")

        delta = 4
        pattern = "/test/url/{}"
        for i in xrange(delta):
            self.client.post(pattern.format(i))
            self.client.get(pattern.format(i+delta))

        responce = self.client.get(reverse('requests'))
        page = responce.content.decode()

        [
            self.assertIn(req, page) for req in [
                pattern.format(i) for i in xrange(delta*2)
            ]
        ]

        self.assertEqual(page.count('POST'), delta)
        self.assertEqual(page.count('GET') - 1, delta)

        self.client.get(pattern.format(111))
        responce = self.client.get(reverse('requests'))
        page = responce.content.decode()

        self.assertIn(pattern.format(111), page)

    def test_num_of_reqs(self):
        """ check number of reqs on the page title """
        delta = 9
        for i in xrange(delta):
            self.client.put("/false/url")

        responce = self.client.get(reverse('requests'))
        page = responce.content.decode()

        self.assertIn("("+str(delta+1)+")", page)