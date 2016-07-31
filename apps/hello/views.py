import json
import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from apps.hello.models import MyData, RequestKeeperModel


def contact_data(request):
    data = MyData.objects.first()
    logging.basicConfig(filename='cont.log', level=logging.DEBUG)
    logging.debug(data)
    return render(request, 'contacts.html', {'data': data})


#def requests_data(request, order='dafault'):

#   requests = [
 #       'GET /requests/ 200',
#       'GET /edit/add/ 200',
  #      'GET /img/upload/img1.png 304',
  #      'GET /img/upload/img2.png 404',
  #      'GET /requests/ 200',
   #     'GET / 200',
  #      'GET /requests/ 200',
  #      'GET / 200',
  #      'GET /requests/ 200',
  #      'GET /edit/ 200']
  #  return render(request, 'requests.html', {'requests': requests[-10:]}) """


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