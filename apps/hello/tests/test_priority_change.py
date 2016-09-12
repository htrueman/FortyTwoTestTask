from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.hello.models import RequestKeeperModel


class RequestsPriority(TestCase):
    def test_ajax_post(self):
        """ test for form ability to save data """
        self.client.login(username='admin', password='admin')
        RequestKeeperModel.objects.create(
            name='/test_path/',
            status=200,
            method='GET',
        )
        self.client.get(reverse('requests'))
        self.client.post(reverse('requests'),
                         data={'priority': 100,
                               'pk': 1}, follow=True)
        self.assertEqual(RequestKeeperModel.objects.first().priority, 100)

    def test_form_displaying_errors(self):
        """ test if form displaying errors with not valid data """
        self.client.login(username='admin', password='admin')
        RequestKeeperModel.objects.create(
            name='/test_path/',
            status=200,
            method='GET',
        )
        response = self.client.post(reverse('requests'),
                                    data={'priority': 'bad',
                                          'pk': 1}, follow=True)
        self.assertFormError(response, 'req_form', 'priority',
                             [u'Enter a whole number.'])

    def test_changing_priority_by_anonynous_user(self):
        """
        test if anounymous user 
        priority changes won't save in model
        """
        RequestKeeperModel.objects.all().delete()
        RequestKeeperModel.objects.create(
            name='/test_path/',
            status=200,
            method='GET',
        )
        self.client.get(reverse('requests'))
        self.client.post(reverse('requests'),
                         data={'priority': 100,
                               'pk': 1}, follow=True)
        self.assertNotEqual(RequestKeeperModel.objects.first().priority, 100)

    def test_ordering_by_priority(self):
        """ test requests ordering by priority """
        for i in range(20):
            RequestKeeperModel.objects.create(
                name='/' + str(i) + '/',
                status=200,
                method='GET',
                priority=i
            )
        response = self.client.get(reverse('requests'))
        RequestKeeperModel.objects.last().delete()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(RequestKeeperModel.objects.all().
                              order_by('-priority', '-pk'))[:10],
                         list(response.context['requests']))
