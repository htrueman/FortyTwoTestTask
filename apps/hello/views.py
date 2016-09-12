import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.hello.forms import EditForm, ChangeReqsPrior
from apps.hello.models import MyData, RequestKeeperModel
from apps.hello.utils import (reqs_ordering, reqs_last_unread_item,
                              reqs_errs, reqs_if_ajax, reqs_last_item,
                              edit_proc)


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
        if req_form.is_valid() and request.user.is_authenticated():
            req_form.save()
            return reqs_if_ajax(request)
        else:
            if request.is_ajax() or not request.user.is_authenticated():
                return reqs_errs(request, req_form)
    if request.is_ajax():
        return reqs_last_unread_item(request)
    last = reqs_last_item(requests)
    return render(request, 'requests.html', {
        'requests': requests,
        'req_form': req_form,
        'last_unread_item': last,
        'sort': order
    })


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
