from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Usuarios
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

# Perfil Completo Del Usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
    

# Crear Perfil De Usuario Por Defecto Cuando el Usuario Se Registra 
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()

# Automatizar Los Perfiles
post_save.connect(create_profile, sender=User)


# Negocios/locales/tiendas
class LugarAdopcion(models.Model):
    name = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Lugares de Adopcion'


# Tipo/Especie de los animales
class Tipo(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'tipos'


class Mascota(models.Model):
    name = models.CharField(max_length=50)
    tamano = models.CharField(max_length=10)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, default=1)
    edad = models.CharField(max_length=10, default='', blank=True, null=False)
    sexo = models.CharField(max_length=10)
    descripcion = models.TextField(max_length=250, default='')
    lugar_adopcion = models.ForeignKey(LugarAdopcion, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='uploads/mascota/')
    
    def __str__(self):
        return self.name
    

class Vacuna(models.Model):
    nombre_vacuna = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_vacuna


class MascotaVacuna(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    fecha_aplicacion = models.DateTimeField()
    fecha_proxima = models.DateTimeField()

    def __str__(self):
        return f"{self.mascota.name} - {self.vacuna.nombre_vacuna}"
