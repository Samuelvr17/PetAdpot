from django.contrib import admin
from django.urls import path
from . import views
from solicitud.views import GestionarSolicitudesView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('update_password/', views.update_password, name='update_password'),
    path('mascota/<int:pk>', views.mascota, name='mascota'),
    path('tipo/<str:foo>', views.tipo, name='tipo'),
    path('tipo_summary/', views.tipo_summary, name='tipo_summary'),
    path('search/', views.search, name='search'),
    path('lista_mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('lista_lugares/', views.lista_lugares, name='lista_lugares'),
    path('gestionar-solicitudes/', GestionarSolicitudesView.as_view(), name='gestionar_solicitudes'),
    path('agregar_vacuna/', views.agregar_vacuna, name='agregar_vacuna'),
     path('agregar_vacuna_mascota/', views.agregar_vacuna_mascota, name='agregar_vacuna_mascota'),


    # CRUD de Mascotas
    path('tipo-mascota/nuevo/', views.crear_tipo_mascota, name='crear_tipo_mascota'),
    path('mascota/nueva/', views.crear_mascota, name='crear_mascota'),
    path('mascota/editar/<int:pk>/', views.editar_mascota, name='editar_mascota'),
    path('mascota/editar/', views.editar_mascota, name='buscar_mascota'),
    path('mascota/eliminar/<int:pk>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('mascota/eliminar/', views.eliminar_mascota, name='buscar_mascota_eliminar'),


    # CRUD de Lugares de Adopción
    path('lugar/nuevo/', views.crear_lugar, name='crear_lugar'),
    path('lugar/editar/<int:pk>/', views.editar_lugar, name='editar_lugar'),
    path('lugar/editar/', views.editar_lugar, name='buscar_lugar'),
    path('lugar/eliminar/<int:pk>/', views.eliminar_lugar, name='eliminar_lugar'),
    path('lugar/eliminar/', views.eliminar_lugar, name='buscar_lugar_eliminar'),
]