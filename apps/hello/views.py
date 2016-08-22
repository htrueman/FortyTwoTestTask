import json
import logging

from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

from apps.hello.forms import EditForm
from apps.hello.models import MyData, RequestKeeperModel


def contact_data(request):
    data = MyData.objects.first()
    logging.debug(data)
    return render(request, 'contacts.html', {'data': data})


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
