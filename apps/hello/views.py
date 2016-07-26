from django.shortcuts import render

def contact_data(request):
	return render(request, 'hello/contacts.html', {})