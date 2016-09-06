from django.test import TestCase

from apps.hello.models import Signal, RequestKeeperModel


class SignalHandlerTests(TestCase):
    def test_sh_hande_create_signal(self):
        " check create signal catches "
        before_counter = Signal.objects.count()
        RequestKeeperModel.objects.create(method='GET', name='/')
        after_counter = Signal.objects.count()

        self.assertEqual(before_counter + 1, after_counter)
        latest_signal = Signal.objects.last()
        self.assertEqual(latest_signal.action, 'create')

    def test_sh_handle_delete_signal(self):
        "check delete signal catches"
        before_counter = Signal.objects.count()
        request_object = RequestKeeperModel.objects.create(
            method='GET', name='/')
        request_object.delete()
        after_counter = Signal.objects.count()

        self.assertEqual(before_counter + 2, after_counter)
        latest_signal = Signal.objects.last()
        self.assertEqual(latest_signal.action, 'delete')

    def test_sh_handle_save_signal(self):
        " check update signal catches "
        before_counter = Signal.objects.count()
        request_object = RequestKeeperModel.objects.create(
            method='GET', name='/')
        request_object.method = 'POST'
        request_object.save()
        after_counter = Signal.objects.count()

        self.assertEqual(before_counter + 2, after_counter)
        latest_signal = Signal.objects.last()
        self.assertEqual(latest_signal.action, 'update')
