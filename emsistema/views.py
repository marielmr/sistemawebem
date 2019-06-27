from django.shortcuts import render
from django.utils import timezone
from . models import person
from . forms import Createuser

# Create your views here.
def login(request):
	posts=person.objects.filter(lastname='lopez').order_by('idperson')
	return render(request,'emsistema/login.html', {'posts': posts})

def uregistry(request):
	if request.method=="POST":
		form=Createuser(request.POST)
		if form.is_valid():
			person=form.save(commit=False)
			person.save()
			return redirect('emsistema.views.login', pk=person.pk)
	else:
		form=Createuser()
	return render(request,'emsistema/user_registry.html',{'form':form})