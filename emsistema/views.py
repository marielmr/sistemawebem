from django.shortcuts import render
from django.utils import timezone
from . models import person

# Create your views here.
def login(request):
	posts=person.objects.filter(lastname='lopez').order_by('idperson')
	return render(request,'emsistema/login.html', {'posts': posts})