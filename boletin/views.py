from django.shortcuts import render
from .forms import RegistradoForm
from .models import Registrado

# Create your views here.
def inicio(request):
	titulo = "Bienvenidos"
	form = RegistradoForm(request.POST or None, request.FILES or None)
	queryset = Registrado.objects.all()

	for obj in queryset:
		print (obj.nombre)
		print (obj.email)
		print (obj.id)

	context = {
		"titulo" : titulo,
		"form" : form,
		"queryset" :queryset
	}

	if form.is_valid():
		#form.save():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		form.save()
		#print (instance.email)
		#print (instance.timestap)
	#if request.user.is_authenticated():
	#	titulo = "Hola, %s!" %(request.user)
		context = {
			"titulo": "Gracias %s, ya se ha registrado" %(nombre)
		}
		if not nombre:
			context = {
				"titulo": "Gracias %s, ya se ha registrado" %(email)
			}
#def inicio(request):
#	form = RegistradoForm(request.POST or None)
#	context = {
#		"form":form
#	}

#	if form.is_valid():
#		form_data = form.cleaned_data
#		abc = form_data.get("nombre_form")
#		obj = Registrado.objects.create(nombre=abc)


	return render(request, "inicio.html", context)

def nosotros(request):
	titulo = "Sobre nosotros"
	
	context = {
		"titulo" : titulo,
	}


	return render(request, "nosotros.html", context)
