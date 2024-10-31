from django.contrib import admin
from .models import  Customer, Profile, Mascota, Tipo, LugarAdopcion, Vacuna, MascotaVacuna
from django.contrib.auth.models import User


#admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(LugarAdopcion)
admin.site.register(Mascota)
admin.site.register(Tipo)
admin.site.register(Vacuna)
admin.site.register(MascotaVacuna)

# Unir la Info de Profile y User
class ProfileInline(admin.StackedInline):
	model = Profile
	
# Ampliar Modelo de Usuario
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

# Anular Registro Anterior forma
admin.site.unregister(User)

# Hacer Registro Nueva Forma
admin.site.register(User, UserAdmin)
