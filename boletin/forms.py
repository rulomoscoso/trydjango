# coding=utf-8

from django import forms
from .models import Registrado

class RegistradoForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre" ,"email", "media"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		#if not ".edu" in email:
		#	raise forms.ValidationError("Por favor utilice un email con la extensión .edu")
		email_base, proveedor = email.split("@")
		dominio, extension = proveedor.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Por favor utilice un email con la extensión .edu")
		return email

#class RegForm(forms.Form):
#	nombre_form = forms.CharField(max_length=100)
#	edad = forms.IntegerField()