# views.py de la aplicación 'solicitud'
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Mascota, Pregunta, RespuestaSolicitud, SolicitudAdopcion

class CuestionarioAdopcionView(View):
    def get(self, request, mascota_id):
        mascota = get_object_or_404(Mascota, id=mascota_id)
        preguntas = Pregunta.objects.all()  # Obtener todas las preguntas
        return render(request, 'cuestionario_adopcion.html', {
            'mascota': mascota,
            'preguntas': preguntas,
        })


from django.shortcuts import redirect

class GuardarSolicitudAdopcionView(View):
    def post(self, request, mascota_id):
        mascota = get_object_or_404(Mascota, id=mascota_id)
        solicitud = SolicitudAdopcion.objects.create(usuario=request.user, mascota=mascota)

        for pregunta in Pregunta.objects.all():
            respuesta_texto = request.POST.get(f'respuesta_{pregunta.id}')
            RespuestaSolicitud.objects.create(solicitud_adopcion=solicitud, pregunta=pregunta, respuesta=respuesta_texto)

        # Redirigir a una página de éxito o la página de detalles de la mascota
        return redirect('home')


class GestionarSolicitudesView(View):
    def get(self, request):
        solicitudes = SolicitudAdopcion.objects.filter(estado__isnull=True)
        return render(request, 'gestionar_solicitudes.html', {'solicitudes': solicitudes})

    def post(self, request):
        solicitud_id = request.POST.get('solicitud_id')
        accion = request.POST.get('accion')
        solicitud = SolicitudAdopcion.objects.get(id=solicitud_id)

        if accion == 'aceptar':
            solicitud.estado = 'aceptada'
        elif accion == 'rechazar':
            solicitud.estado = 'rechazada'
        solicitud.save()
        return redirect('gestionar_solicitudes')