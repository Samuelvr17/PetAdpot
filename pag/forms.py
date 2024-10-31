from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile, Mascota, LugarAdopcion


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['name', 'tamano', 'tipo', 'edad', 'sexo', 'descripcion', 'lugar_adopcion', 'image']
        labels = {
            'name': '',
            'tamano': '',
            'tipo': '',
            'edad': '',
            'sexo': '',
            'descripcion': '',
            'lugar_adopcion': '',
            'image': '',
        }

    def __init__(self, *args, **kwargs):
        super(MascotaForm, self).__init__(*args, **kwargs)
        
        # Agregamos la clase 'form-control' y los placeholders a cada campo
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre de la mascota'})
        self.fields['tamano'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tamaño de la mascota'})
        self.fields['tipo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tipo de mascota (Perro, Gato, etc.)'})
        self.fields['edad'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Edad de la mascota'})
        self.fields['sexo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sexo de la mascota'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descripción de la mascota'})
        self.fields['lugar_adopcion'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Lugar de adopción'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Subir imagen de la mascota'})



class LugarAdopcionForm(forms.ModelForm):
    class Meta:
        model = LugarAdopcion
        fields = ['name', 'ubicacion', 'telefono']
        labels = {
            'name': '',
            'ubicacion': '',
            'telefono': '',
        }

    def __init__(self, *args, **kwargs):
        super(LugarAdopcionForm, self).__init__(*args, **kwargs)
        
        # Agregamos la clase 'form-control' y los placeholders a cada campo
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre del Lugar de Adopción'})
        self.fields['ubicacion'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ubicación del Lugar'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Teléfono de Contacto'})



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UpdateUserForm(UserChangeForm):
	# Ocultar la contraseña
	password = None

	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'


class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1', 'new_password2']

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), required=False)
    address = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}), required=False)
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=False)
    country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=False)
    zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}), required=False)

    class Meta:
        model = Profile
        fields = ('phone', 'address', 'city', 'country', 'zipcode')