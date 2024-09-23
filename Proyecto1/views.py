from django.http import HttpResponse
import datetime

def saludo(request):

    documento = """
        <html>
        <body>
        <h2>
        Hola cabezón, ¿estás aprendiendo algo?
        <h2/>
        <body/>
        <html/>
        """
    return HttpResponse(documento)

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


