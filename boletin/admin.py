from django.contrib import admin

# Register your models here.
from .models import Registrado
from .forms impoert RegistradoForm

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "codigo_postal", "timestap", "actualizado"]
	form = RegistradoForm
	#class Meta:
	#	model = Registrado

admin.site.register(Registrado, AdminRegistrado)
