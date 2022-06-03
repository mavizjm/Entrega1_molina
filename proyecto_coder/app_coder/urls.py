from django.urls import path
from . import views

urlpatterns = [

    path("cursos" , views.cursos , name= "cursos"),
    path("profesores" , views.profesores , name= "profesores"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos" , views.alumnos , name = "alumnos"),
    path("contacto" , views.contacto),
    path("" , views.inicio),
    path("alta_curso" , views.curso_formulario),
    path("buscar_curso" , views.buscar_curso),
    path("buscar" , views.buscar ),
    path("alta_profesor" , views.profesor_formulario),
    path("alta_alumno" , views.alumno_formulario)
]


