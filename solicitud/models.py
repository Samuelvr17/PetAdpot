"""
from django.db import models
from django.contrib.auth.models import User
from pag.models import Mascota


# Model de Solicitud de adopción

class SolicitudAdopcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False) # True - aprobado y False - rechazada


    def __str__(self):
        return f"Solicitud de {self.usuario.username} para {self.mascota.name}"


        
# Model del Cuestionario para hacer solicitud

class Cuestionario(models.Model):
    solicitud_adopcion = models.OneToOneField(SolicitudAdopcion, on_delete=models.CASCADE, related_name='cuestionario')
    pregunta_1 = models.TextField(verbose_name="¿Por qué desea adoptar una mascota?")
    pregunta_2 = models.TextField(verbose_name="¿Quién será el responsable de la mascota?")
    pregunta_3 = models.TextField(verbose_name="¿Qué haría si la mascota llega a enfermarse?")
    pregunta_4 = models.TextField(verbose_name="Si tiene un viaje, ¿con quién quedaría la mascota?")
    pregunta_5 = models.TextField(verbose_name="¿Ya había adoptado una mascota antes?")
    pregunta_6 = models.TextField(verbose_name="¿En su hogar ya hay alguna otra mascota, cuál?")

    def __str__(self):
        return f"Cuestionario de {self.solicitud_adopcion.usuario.username}"
"""