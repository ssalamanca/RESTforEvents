from rest_framework import serializers
from .models import DateDimension
class DateDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateDimension
        fields = ('fechaInicio','fechaFin','tag')

class StringListField(serializers.Serializer): #Intento de serializador para devolver una lista de Strings, todavia no funciona
     value = serializers.ListField(child=serializers.StringRelatedField())