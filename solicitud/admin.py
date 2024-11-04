from django.contrib import admin
from .models import SolicitudAdopcion, Pregunta, RespuestaSolicitud

@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mascota', 'fecha_solicitud', 'estado')
    list_filter = ('estado', 'fecha_solicitud')
    search_fields = ('usuario__username', 'mascota__name')
    ordering = ('-fecha_solicitud',)

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto_preguntas',)
    search_fields = ('texto_preguntas',)

@admin.register(RespuestaSolicitud)
class RespuestaSolicitudAdmin(admin.ModelAdmin):
    list_display = ('solicitud_adopcion', 'pregunta', 'respuesta')
    search_fields = ('solicitud_adopcion__usuario__username', 'pregunta__texto_preguntas')

