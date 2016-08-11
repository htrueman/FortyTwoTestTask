import json
import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.generic import ListView

from apps.hello.forms import EditForm
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
                'date': req.date.strftime("%Y-%m-%d %H:%M:%S.%f"),
                'author': req.author
            } for req in requests
        ]
    })
    return HttpResponse(response_data, content_type='application/json')


@login_required()
def edit_contacts(request):
    info = MyData.objects.first()
    if not info:
        return render(request, 'edit_contacts.html',
                      {'nothing': 'No data to edit'})
    if request.method == 'POST':
        form = EditForm(
          request.POST,
          request.FILES,
          instance=info)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse('OK')
            else:
                return render(request, 'edit_contacts.html', {'form': form})
        else:
            if request.is_ajax():
                errors_dict = {}
                if form.errors:
                    for error in form.errors:
                        err = form.errors[error]
                        errors_dict[error] = unicode(err)
                return HttpResponseBadRequest(json.dumps(errors_dict))
            else:
                message = 'Fail'
                return render(request, 'edit_contacts.html',
                              {'form': form, 'message': message})
    else:
        form = EditForm(instance=info)
        return render(request, 'edit_contacts.html', {'form': form})
