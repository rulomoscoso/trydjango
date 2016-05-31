from django.shortcuts import render
from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
	form = RegForm(request.POST or None)
	context = {
		"form":form
	}

	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("nombre_form")
		obj = Registrado.objects.create(nombre=abc)


	return render(request, "inicio.html", context)
