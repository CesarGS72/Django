from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

def saludo(request):

    nombre = 'César'
    apellido = 'Gómez Sánchez'
    ahora = datetime.datetime.now().time
    temas = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']

    #doc_externo = open('C:/Users/Cesar Gomez/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/mi_plantilla.html')
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo = get_template('mi_plantilla.html')

    ctx = {'nombre_alumno': nombre, 'apellido_alumno': apellido, 'hora_actual':ahora, 'temario':temas}
    
    #documento = doc_externo.render(ctx)

    return render(request, 'mi_plantilla.html', ctx)


def despedida(request):

    return HttpResponse("Pues ya va siendo hora de descansar.")

def dame_fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = f"""
        <html>
        <body>
        <h2>
        Fecha y hora actuales: {fecha_actual}
        <h2/>
        <body/>
        <html/>
        """

    return HttpResponse(documento)

def calcula_edad(request, agno, agnofuturo):
    agno_actual = datetime.datetime.now().year
    edad = agno + (agnofuturo-agno_actual)
    documento = f"""
        <html>
        <body>
        <h2>
        En el año {agnofuturo} tendrás {edad} años.
        <h2/>
        <body/>
        <html/>
        """
    return HttpResponse(documento)

def moxeta(request):

    fecha_actual = datetime.datetime.now()
    return render(request, "su_cuchita.html", {"dame_fecha":fecha_actual})

def sofalete(request):

    fecha_actual = datetime.datetime.now()
    return render(request, "su_sofa.html", {"dame_fecha":fecha_actual})