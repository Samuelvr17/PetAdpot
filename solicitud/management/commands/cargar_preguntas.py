from django.core.management.base import BaseCommand
from solicitud.models import Pregunta

class Command(BaseCommand):
    help = 'Carga las preguntas predeterminadas para las solicitudes de adopción.'

    def handle(self, *args, **kwargs):
        preguntas_texto = [
            "¿Por qué desea adoptar una mascota?",
            "¿Quién será el responsable de la mascota?",
            "¿Qué haría si la mascota llega a enfermarse?",
            "Si tiene un viaje, ¿con quién quedaría la mascota?",
            "¿Ya había adoptado una mascota antes?",
            "¿En su hogar ya hay alguna otra mascota, cuál?"
        ]

        for texto in preguntas_texto:
            Pregunta.objects.get_or_create(texto_preguntas=texto)
        self.stdout.write(self.style.SUCCESS('Preguntas cargadas exitosamente.'))
