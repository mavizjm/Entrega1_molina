from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from app_coder.forms import Curso_formulario
from app_coder.models import Profesor
from app_coder.forms import Profesor_formulario
from app_coder.forms import Alumno_formulario
from app_coder.models import Alumno


# Create your views here.

def inicio(request):

    return render(request , "plantillas.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)

    return HttpResponse(documento)

def alta_alumno(request , nombre):
    curso = Alumno(nombre=nombre , camada=821354)
    curso.save()
    texto = f"Se guardó en la BD el alumno: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)


def alta_curso(request , nombre):
    curso = Curso(nombre=nombre , camada=821354)
    curso.save()
    texto = f"Se guardó en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)


def alta_profesor(request , nombre):
    curso = Profesor(nombre=nombre , camada=821354)
    curso.save()
    texto = f"Se guardó en la BD el profesor: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)

def alumnos(request):

    return render(request , "alumnos.html")


def contacto(request):

    return render(request , "contacto.html")

def profesores (request):

    return render(request , "profesores.html")

def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data



        curso = Curso(nombre = datos ['nombre'] , camada = datos['camada'])
        curso.save()
        return render(request , "formulario.html")

    return render(request , "formulario.html")

def alumno_formulario(request):

    if request.method == "POST":

        mi_formulario = Alumno_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data



        curso = Alumno(nombre = datos ['nombre'] , camada = datos['camada'])
        curso.save()
        return render(request , "alumnos_formulario.html")

    return render(request , "alumnos_formulario.html")




def profesor_formulario(request):

    if request.method == "POST":

        mi_formulario = Profesor_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data



        curso = Profesor(nombre = datos ['nombre'] , camada = datos['camada'])
        curso.save()
        return render(request , "profesor_formulario.html")

    return render(request , "profesor_formulario.html")   


def buscar_curso(request):

    return render(request , "buscar_curso.html")

def buscar(request):


    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacío")





