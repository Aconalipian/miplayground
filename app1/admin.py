from django.contrib import admin
from .models import *

# Register your models here.

#acá se configura todo lo que queremos que aparezca en el sitio de admin
#django


admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)