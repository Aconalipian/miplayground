from django.shortcuts import render
from .models import Curso
from .models import Estudiante
from .models import Profesor
from .models import Entregable





# Create your views here.
def home(request):
    return render(request, "app1/home.html")





def cursos(request):
    contexto = {'cursos': Curso.objects.all(), 'titulo': 'Reporte de cursos','comisiones' : ['55630', '55640']}
    return render(request, "app1/cursos.html", contexto)

def profesores(request):
    return render(request, "app1/profesores.html")

def estudiantes(request):
    return render(request, "app1/estudiantes.html")

def entregables(request):
    return render(request, "app1/entregables.html")