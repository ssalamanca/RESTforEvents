from django.db import models
from mongoengine import *

# Create your models here.

# Aruba Wifi Models from API.

class AP(models.Model):
    ap_id = models.IntegerField(unique=True)
    client_count = models.IntegerField()
    name = models.CharField(max_length=50)
    ap_group = models.CharField(max_length=100)
    is_up = models.BooleanField(default=False)
    mac_address = models.CharField(max_length=50)

    def __str__(self):
        return ("- %s | %s | %s | %s | %s | %s" %
                (self.ap_id, self.client_count,
                 self.name, self.ap_group,
                 self.is_up, self.mac_address))

class Client(models.Model):
    client_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=50)
    device_type = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    signal = models.IntegerField()
    role = models.CharField(max_length=100)
    auth_status = models.BooleanField(default=False)
    assoc_status = models.BooleanField(default=False)
    # Intensidad de señal
    rssi = models.IntegerField()
    # Calidad de señal
    snr = models.IntegerField()
    ap = models.ForeignKey(AP, on_delete=models.CASCADE)

class DateDimension(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    #fechaInicio = models.CharField(max_length=100)
    #fechaFin = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    
    def __str__(self):
        return "Evento: ",self.tag," Fecha inicio: ",self.fechaInicio," Fecha fin: ",self.fechaFin