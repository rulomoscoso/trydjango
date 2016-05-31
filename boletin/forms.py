from django import forms
from .models import Registrado

class RegistradoForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["email"]

#class RegForm(forms.Form):
#	nombre_form = forms.CharField(max_length=100)
#	edad = forms.IntegerField()