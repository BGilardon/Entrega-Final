from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

from .models import Avatar




class posteoCrear(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=30)
    cuerpo = forms.CharField(widget=CKEditorWidget())
    fecha = forms.DateField()
    imagen = forms.ImageField(label="imagen", required=False)
    
    

roles = [("usuario", "usuario"), ("administrador", "administrador")]
class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)  # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

