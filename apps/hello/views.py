import json
import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from apps.hello.models import MyData, RequestKeeperModel


def contact_data(request):
    data = MyData.objects.first()
    logging.debug(data)
    return render(request, 'contacts.html', {'data': data})


class RequestKeeperView(ListView):
    model = RequestKeeperModel
    template_name = 'requests.html'
    context_object_name = 'requests'
    queryset = RequestKeeperModel.objects.all()[:10]

    def get_context_data(self, **kwargs):
        context = super(RequestKeeperView, self).get_context_data(**kwargs)
        context['news'] = self.get_queryset().count()
        return context


def check_new_requests(request):
    since = request.GET.get('since', 0)
    count = RequestKeeperModel.objects.filter(pk__gt=since).count()
    response_data = json.dumps({
        'count': count
    })
    return HttpResponse(response_data, content_type='application/json')


def give_new_requests(request):
    count = min(10, (request.GET.get('count', 0)))
    requests = RequestKeeperModel.objects.all()[:count]
    response_data = json.dumps({
        'requests': [
            {
                'pk': req.pk,
                'method': req.method,
                'path': req.path,
                'date': req.date.strftime("%Y-%m-%d %H:%M:%S.%f")
            } for req in requests
        ]
    })
    return HttpResponse(response_data, content_type='application/json')


def edit_contacts(request):
    return render(request, 'edit_contacts.html', {})