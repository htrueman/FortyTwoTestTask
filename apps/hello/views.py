import logging
import datetime
from django.shortcuts import render

from apps.hello.models import MyData


def contact_data(request):
    data = MyData.objects.first()
    errors = {}
    logging.basicConfig(filename='cont.log', level=logging.DEBUG)
    # extra condition for empty db
    if data:
        if data.birthday > datetime.datetime.now().date():
            errors['birthday'] = "Please write your real date of birth!"
            data.birthday = None
            logging.debug(data, errors)
            return render(
                request, 'contacts.html', {'errors': errors, 'data': data})
        else:
            logging.debug(data)
            return render(
                request, 'contacts.html', {'data': data})
    else:
        return render(request, 'contacts.html', {})


def requests_data(request):
    requests = [
        'GET /requests/ 200',
        'GET /edit/add/ 200',
        'GET /img/upload/img1.png 304',
        'GET /img/upload/img2.png 404',
        'GET /requests/ 200',
        'GET / 200',
        'GET /requests/ 200',
        'GET / 200',
        'GET /requests/ 200',
        'GET /edit/ 200']
    return render(request, 'requests.html', {'requests': requests[-10:]})
