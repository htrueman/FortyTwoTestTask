import json

from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

from apps.hello.models import RequestKeeperModel


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


def reqs_errs(req_form):
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
