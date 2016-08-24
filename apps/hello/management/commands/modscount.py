from django.core.management import BaseCommand
from django.db.models import get_models


class Command(BaseCommand):
    help = "Prints number of model objects in a database."

    def handle(self, *args, **options):
        for model in get_models():
            output = 'There are %d objects in %s model' %\
            			(model.objects.count(),
                        	model.__name__)
            self.stdout.write(output)
            self.stderr.write('error: ' + output)
