from django import forms
from . models import person, user

class Createuser(forms.ModelForm):
	class Meta:
		model=person
		fields=('firstname','lastname','birthdate')