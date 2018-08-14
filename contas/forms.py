from .models import Usuario, Telefone
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserAdminForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email']

class UserCreationForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ["username", "nome", "sobrenome", "email", "cpf", "is_staff", "is_active"]

class TelefoneForm(forms.ModelForm):

    class Meta:
        model = Telefone
        fields = ['numero']