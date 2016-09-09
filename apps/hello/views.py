import json
import logging

from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

from apps.hello.forms import EditForm, ChangeReqsPrior
from apps.hello.models import MyData, RequestKeeperModel


def contact_data(request):
    data = MyData.objects.first()
    logging.debug(data)
    return render(request, 'contacts.html', {'data': data})


def requests(request):
    order = request.GET.get('order', '')
    requests = reqs_ordering(order)
    req_form = ChangeReqsPrior()
    if request.method == 'POST':
        pke = request.POST['pk']
        instance = RequestKeeperModel.objects.get(id=pke)
        req_form = ChangeReqsPrior(request.POST, instance=instance)
        if req_form.is_valid():
            req_form.save()
            return reqs_if_ajax(request)
        else:
            if request.is_ajax():
                return reqs_ajax(req_form)
    if request.is_ajax():
        return reqs_last_unread_item(request)
    last = reqs_last_item(requests)
    return render(request, 'requests.html', {
        'requests': requests,
        'req_form': req_form,
        'last_unread_item': last,
        'sort': order
    })


def reqs_ordering(order):
    if order == 'prior':
        return list(RequestKeeperModel.objects.all().
                    order_by('-priority', '-pk'))[:10]
    if order == 'prior_asc':
        return list(RequestKeeperModel.objects.all().
                    order_by('priority', 'pk'))[:10]
    elif order == 'number' or not order:
        return list(RequestKeeperModel.objects.all().
                    order_by('-pk'))[:10]


def reqs_last_unread_item(req):
    if 'last_unread_item' not in req.GET:
        return None
    object = RequestKeeperModel.objects.filter(
        id__gt=int(
            req.GET['last_unread_item'])).order_by('-id')[:10]
    object = list(object)
    data = serialize('json', object)
    return HttpResponse(data, content_type="application/json")


def reqs_ajax(req_form):
    if req_form.errors:
        errors_dict = {}
        if req_form.errors:
            for error in req_form.errors:
                print error
                err = req_form.errors[error]
                errors_dict[error] = unicode(err)
        return HttpResponseBadRequest(json.dumps(errors_dict))
    return 'ERROR'


def reqs_if_ajax(req):
    if req.is_ajax():
        return HttpResponse('OK')
    return HttpResponse('NOT AJAX')


def reqs_last_item(requests):
    last = 0
    for req in requests:
        if req.priority == 0:
            last = req.id
            break
    return last


@login_required()
def edit_contacts(request):
    info = MyData.objects.first()
    if request.method == 'POST':
        form = EditForm(
          request.POST,
          request.FILES,
          instance=info)
        return edit_proc(request, form)
    else:
        form = EditForm(instance=info)
        return render(
                        request, 'edit_contacts.html',
                        {'form': form, 'info': info})


def edit_proc(req, form):
    if form.is_valid():
        form.save()
        if req.is_ajax():
            return HttpResponse('OK')
        else:
            return render(req, 'edit_contacts.html', {'form': form})
    else:
        if req.is_ajax():
            errors_dict = {}
            if form.errors:
                for error in form.errors:
                    err = form.errors[error]
                    errors_dict[error] = unicode(err)
            return HttpResponseBadRequest(json.dumps(errors_dict))
        else:
            message = 'Fail'
            return render(req, 'edit_contacts.html',
                          {'form': form, 'message': message})
    return 'OK'
