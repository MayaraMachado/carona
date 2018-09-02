from django import forms
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import AuthUser

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = AuthUser
        fields = ['username', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', 
        widget= forms.TextInput(attrs = {'placeholder' : 'Username'} )
    )
    password = forms.CharField(label='Password', max_length=16,
        widget = forms.PasswordInput(attrs = {'placeholder':'senha'}, 
        render_value = False),
        # validators=[MinLengthValidator(8, message = 'A senha deve conter ao menos 8 caracteres')]
    )

    def login(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        if  user is not None:
            login(request, user)