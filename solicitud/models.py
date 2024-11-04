from django.db import models
from django.contrib.auth.models import User
from pag.models import Mascota


class SolicitudAdopcion(models.Model):
    ESTADOS = [
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, null=True)

    def __str__(self):
        return f"Solicitud de {self.usuario.username} para {self.mascota.name} - {self.estado or 'Sin decidir'}"


class Pregunta(models.Model):
    texto_preguntas = models.TextField()

    def __str__(self):
        return self.texto_preguntas  # Cambiado para que retorne el texto de la pregunta
    

class RespuestaSolicitud(models.Model):
    solicitud_adopcion = models.ForeignKey(SolicitudAdopcion, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=500)

    def __str__(self):
        return f"Respuesta a '{self.pregunta.texto_preguntas}' en solicitud {self.solicitud_adopcion.id}"
