from django.shortcuts import render

from apps.hello.models import MyData


def contact_data(request):
    data = MyData.objects.first()
    return render(request, 'contacts.html', {'data': data})
