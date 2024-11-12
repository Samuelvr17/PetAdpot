from django.urls import path
from .views import CuestionarioAdopcionView, GuardarSolicitudAdopcionView

app_name = 'solicitud'  

urlpatterns = [
    path('mascota/<int:mascota_id>/cuestionario/', CuestionarioAdopcionView.as_view(), name='cuestionario_adopcion'),
    path('mascota/<int:mascota_id>/guardar_solicitud/', GuardarSolicitudAdopcionView.as_view(), name='guardar_solicitud'),
    

]
