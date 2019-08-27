from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import xml_functions
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint
from .models import DateDimension
from .forms import DateDimensionForm
from .serializers import DateDimensionSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.dateparse import parse_date
import datetime

#Esta va a ser la clase principal donde se va a realizar el tratamiento (Tratamiento.py) que va a recibir todas las peticiones para el tratamiento de los datos

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#CRUD para los eventos mediante django framework. Todo lo que llegue a DateDimensionView ya tiene por defecto opciones para agregar, eliminar, actualizar, mostrar listado, ... segun la petición HTTP
class DateDimensionView(viewsets.ModelViewSet):
    queryset= DateDimension.objects.all()
    serializer_class = DateDimensionSerializer

#Metodo para obtener la lista de tags (sin repetidos) de la base de datos.
@api_view(['GET','POST'])
def tags(request):
    #user = DateDimension.objects.get(id=pk)
    if request.method == 'GET':
        queryset = DateDimension.objects.values_list('tag', flat=True).order_by().distinct()
        #print(queryset)
        #data = getattr(user, fname)
        #print(request.GET['tag'])
        print(request.body)
        return Response({'tags':queryset})
    elif request.method == 'POST':
        #print(request.POST['"fechaInicio"'])
        print(request.POST)

#Entradas: Fecha de inicio y fecha final que llegan por el metodo GET
@api_view(['GET']) 
def tags_date_range(request):
    #temp_date = parse_date(date_str)
    #fechaIni='2019-08
    #fechaFin='2019-08-18'
    #queryset = DateDimension.objects.exclude(fechaInicio__lt=fechaIni, fechaFin__gt=fechaFin)  
    return Response({'tags':consultaBDTags(request.GET['fechaInicio'],request.GET['fechaFin'])})

def consultaBDTags(fechaIni, fechaFin):
    queryset = DateDimension.objects.filter(fechaInicio__gte=fechaIni, #El gte es greater than y lte es less than. Se hacer de la siguiente forma: nombreAtributo__gte
                                fechaFin__lte=fechaFin).values_list('tag', flat=True).order_by().distinct() # Esto debe hacerlo la parte de Persistencia
    #El queryset devuelve una lista de tags. La lista se recorre normal como cualquier lista.
    """for item in queryset:
        print(item)""" 
    return queryset

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#TODO Hacer un metodo tratamiento que es el que va a recibir las peticiones para los modelos que necesiten solo datos que se encuentren en la bd
#Entradas:Nombre del servicio
#Salidas: El objeto resultante despues de la limpieza y la preparación. Si en la preparación se tienen qu agregar nuevos campos toca mirar si se crea un nuevo...->
#...-> objeto con esos campos. (Pensar en la opción de usar DataFrames)
#TODO Hacer un metodo para la conexión a la bd

#TODO Hacer una funcion que va a ser la que convierta los datos que llegan de la bd en el objeto según el servicio


#TODO La funcion de unir_fuentes debe recibir el nombre del servicio y la direccion en donde están ubicadas las fuentes que se van a unir
#Es importante recibir el nombre del servicio para así distinguir a que metodo se va a llamar para la clase de "Union_fuentes" y ahí hacer la creacion de las respectivas clases
#Salidas: El objeto resultante de la union de las fuentes. (Habria que crear un objeto en el archivo de models.py por cada resultado de la union de archivos)
def unir_fuentes(self):
    xml_functions.union_fuentes('C:\\Users\\santiago.salamanca\\OneDrive - Accenture\\Universidad\\Tesis\\Tests\\TestXML\\treatingxml\\samples\\example_clientdetail.xml','C:\\Users\\santiago.salamanca\\OneDrive - Accenture\\Universidad\\Tesis\\Tests\\TestXML\\treatingxml\\samples\\students.xml','clients','key2')
    #xml_functions.union_fuentes('C:\\Users\\santiago.salamanca\\OneDrive - Accenture\\Universidad\\Tesis\\Tests\\TestXML\\treatingxml\\samples\\test1.xml','C:\\Users\\santiago.salamanca\\OneDrive - Accenture\\Universidad\\Tesis\\Tests\\TestXML\\treatingxml\\samples\\test2.xml','food','dish')
    return HttpResponse('Hecho')


#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Prueba con conexión a servidor de mongo online
def pruebamongo(self):
    client = MongoClient("mongodb+srv://admonbd:admonbd@cluster0-vl6gj.mongodb.net/test?retryWrites=true&w=majority")
    db=client.admin
    # Issue the serverStatus command and print the results
    db=client.pruebaFechas
    #Step 2: Create sample data
    fechaInicio = ['01-08-2019','02-08-2019','03-08-2019','04-08-2019','05-08-2019']
    fechaFin = ['12-10-2019','01-10-2019','12-10-2019','22-10-2019','28-10-2019','13-10-2019','19-10-2019','08-10-2019']
    tags = ['SEMANA_PARCIALES','FESTIVO']
    for x in range(1, 11):
        business = {
            'fechaInicio' : fechaInicio[randint(0, (len(fechaInicio)-1))],
            'fechaFin' : fechaFin[randint(0, (len(fechaFin)-1))],
            'tag' : tags[randint(0, (len(tags)-1))]
        }
        #Step 3: Insert business object directly into MongoDB via insert_one
        result=db.fechas.insert_one(business)
        #Step 4: Print to the console the ObjectID of the new document
        print('Created {0} of 10 as {1}'.format(x,result.inserted_id))
    #Step 5: Tell us that you are done
    print('finished creating 10 fechas')
    return HttpResponse("Revisar servidor")

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Parte del front. CRUD para los eventos.
def date_list(request):
    print("lista")
    fechas = DateDimension.objects.all()
    for field in fechas:
        print('fechaInicio ',field.fechaInicio)
    return render(request,"fechas.html",{'fechas':fechas})
def create_date(request):
    print("crear fecha")
    form = DateDimensionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('date_list')
    return render(request, 'fechas-form.html',{'form':form})
def update_date(request,id):
    print("actualizar fecha")
    fecha = DateDimension.objects.get(id=id)
    form = DateDimensionForm(request.POST or None, instance=fecha)
    if form.is_valid():
        form.save()
        return redirect('date_list')
    return render(request,'fechas-form.html',{'form':form,'fecha':fecha})
def delete_date(request,id):
    print("borrar lista")
    fecha = DateDimension.objects.get(id=id)
    if request.method== 'POST':
        fecha.delete()
        return redirect('date_list')
    return render(request,'fecha-delete-confirm.html',{'fecha':fecha})

