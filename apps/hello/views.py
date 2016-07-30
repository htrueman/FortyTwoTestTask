import logging
from django.shortcuts import render

from apps.hello.models import MyData


def contact_data(request):
    data = MyData.objects.first()
    logging.basicConfig(filename='cont.log', level=logging.DEBUG)
    logging.debug(data)
    return render(request, 'contacts.html', {'data': data})
