from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UserInfoForm, UpdateUserForm, ChangePasswordForm, MascotaForm, LugarAdopcionForm
from .models import Mascota, Tipo, Profile, LugarAdopcion
from django.contrib.auth.models import User
from django.db.models import Q


# Crear nueva mascota
def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota creada exitosamente.')
            return redirect('home')
    else:
        form = MascotaForm()
    return render(request, 'formulario_mascota.html', {'form': form})

# Editar mascota existente
def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota actualizada exitosamente.')
            return redirect('home')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'formulario_mascota.html', {'form': form})

# Eliminar mascota
def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    mascota.delete()
    messages.success(request, 'Mascota eliminada exitosamente.')
    return redirect('home')

# Crear nuevo lugar de adopción
def crear_lugar(request):
    if request.method == 'POST':
        form = LugarAdopcionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lugar de adopción creado exitosamente.')
            return redirect('home')
    else:
        form = LugarAdopcionForm()
    return render(request, 'formulario_lugar.html', {'form': form})

# Editar lugar de adopción existente
def editar_lugar(request, pk):
    lugar = get_object_or_404(LugarAdopcion, pk=pk)
    if request.method == 'POST':
        form = LugarAdopcionForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lugar de adopción actualizado exitosamente.')
            return redirect('home')
    else:
        form = LugarAdopcionForm(instance=lugar)
    return render(request, 'formulario_lugar.html', {'form': form})

# Eliminar lugar de adopción
def eliminar_lugar(request, pk):
    lugar = get_object_or_404(LugarAdopcion, pk=pk)
    lugar.delete()
    messages.success(request, 'Lugar de adopción eliminado exitosamente.')
    return redirect('home')


def home(request):
    return render(request, 'home.html', {})

def lista_lugares(request):
    lugares_adopcion = LugarAdopcion.objects.all() 
    return render(request, 'lista_lugares.html', {'lugares_adopcion': lugares_adopcion})

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'lista_mascotas.html', {'mascotas':mascotas})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, ('Ha Iniciado Seión'))
            return redirect('home')
        else:
            messages.success(request, ("Hubo Un Error, Inténtelo De Nuevo"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("Ha Cerrado La Sesión"))
    return redirect('home')
    

def register_user(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Perfil Creado - Rellene Sus Datos De Usuario"))
            return redirect('home')
        else:
            messages.success(request, ("Hubo Un Error, Inténtelo De Nuevo"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})
    

def tipo(request, foo):
    # reemplazar guiones con espacios
    foo = foo.replace('-', ' ')
    try:
        tipo = Tipo.objects.get(name=foo)
        mascotas = Mascota.objects.filter(tipo=tipo)
        return render(request, 'tipo.html', {'mascotas': mascotas, 'tipo': tipo})
    except:
        messages.success(request, ("Por ahora NO hay Mascotas de este Tipo"))
        return redirect('home')
    

def tipo_summary(request):
    tipos = Tipo.objects.all()  
    return render(request, 'tipo_summary.html', {'tipos':tipos})


def mascota(request, pk):
    mascota = Mascota.objects.get(id=pk)
    return render(request, 'mascota.html', {'mascota': mascota})


def update_info(request):
    if request.user.is_authenticated:
        # Obtener el Usuario Actual
        current_user = Profile.objects.get(user__id=request.user.id)
        # Formulario de Usuario
        form = UserInfoForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, ("Su información ha sido actualizada"))
            return redirect('home') 
        return render(request, 'update_info.html', {'form':form})
    else:
        messages.success(request, "Debe iniciar sesión para acceder a esta página")
        return redirect('home')  
    

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, ("Su Perfil Ha Sido Actualizado"))
            return redirect('home') 
        return render(request, 'update_user.html', {'user_form':user_form})
    else:
        messages.success(request, "Debe iniciar sesión para acceder a esta página")
        return redirect('home')
    

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Su Contraseña ha sido actualizada")
                login(request, current_user)
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        else:
            form = ChangePasswordForm(current_user) 
        return render(request, 'update_password.html', {'form':form})
    else:  
        messages.success(request, "Debe iniciar sesión para acceder a esta página")
    return redirect('home')


def search(request):
	if request.method == "POST":
		searched = request.POST['searched']
		searched = Mascota.objects.filter(Q(name__icontains=searched) | Q(tamano__icontains=searched) | Q(edad__icontains=searched) | Q(sexo__icontains=searched) | Q(descripcion__icontains=searched))
		if not searched:
			messages.success(request, "Ese Producto No Existe. Inténtelo de Nuevo.")
			return render(request, "search.html", {})
		else:
			return render(request, "search.html", {'searched':searched})
	else:
		return render(request, "search.html", {})