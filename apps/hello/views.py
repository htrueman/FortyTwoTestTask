import datetime
from django.shortcuts import render

from apps.hello.models import MyData


def contact_data(request):
    data = MyData.objects.first()
    errors = {}
    context = MyData(request, {})
    # extra condition for empty db
    if data:
        if data.birthday > datetime.datetime.now().date():
            errors['birthday'] = "Please write your real date of birth!"
            data.birthday = None
            return render(request, 'contacts.html', {'errors': errors, 'data': data})
        else:
            return render(request, 'contacts.html', {'data': data})
    else:
        return render(request, 'contacts.html', {})
