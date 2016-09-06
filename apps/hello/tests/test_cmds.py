from django.core.management import call_command
from django.db.models import get_models
from django.utils.six import BytesIO
from django.test import TestCase


class ModelCountTest(TestCase):
    def test_cmd_output(self):
        """ test command output"""
        output = BytesIO()
        errout = BytesIO()
        call_command('modscount',
                     stdout=output,
                     stderr=errout)
        for model in get_models():
            err_str = 'error: There are {} objects in {} model'.format(
                model.objects.count(),
                model.__name__
            )
            out_str = 'There are {} objects in {} model'.format(
                model.objects.count(),
                model.__name__
            )
            self.assertIn(err_str, errout.getvalue())
            self.assertIn(out_str, output.getvalue())
