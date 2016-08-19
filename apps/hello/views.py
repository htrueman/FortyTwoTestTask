import json
import logging

from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
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


def requests(request):
    if request.is_ajax():
        if 'last_unread_item' not in request.GET:
            return None
        object = RequestKeeperModel.objects.filter(
            id__gt=int(
                request.GET['last_unread_item'])).order_by('-id')[:10]
        object = list(object)
        data = serialize('json', object)
        return HttpResponse(data, content_type="application/json")
    requests = RequestKeeperModel.objects.all().order_by('-id')[:10]
    last = requests[0].id if requests else 0
    return render(request, 'requests.html', {
        'requests': requests,
        'last_unread_item': last
    })
