from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('',views.DateDimensionView)
#router.register('get_tags',views.TagsView)

urlpatterns = [
    path('', views.index, name='index'), #Llama al metodo de index encontrado en la vista
    path ('unir_fuentes',views.unir_fuentes),
    path('prueba_mongo',views.date_list,name="date_list"),
    path('prueba_mongo/create',views.create_date,name="create_date"),
    path('prueba_mongo/update/<int:id>/',views.update_date,name="update_date"),
    path('prueba_mongo/delete/<int:id>/',views.delete_date,name="delete_date"),
    path('rest_fechas',include(router.urls)),
    path('get_tags/', views.tags, name='get_tags'), # Lo que esta dentro del as_view() es para definir a que metodo debe ir--->
    #-->Dependiendo de la petición http que se reciba.
    path('get_tags_range/', views.tags_date_range, name='get_tags_range'),
]