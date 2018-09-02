from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserAdminCreationForm, LoginForm
from django.views import generic
from django.urls import reverse_lazy
from .models import AuthUser
from django.contrib.auth import logout


class RegisterView(CreateView):
    model = AuthUser
    template_name = 'register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


def Login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print('entrou login')
        form.login(request)
        return render(request, 'index.html')
    return render(request, 'login.html', {'form': form})

def Logout_View(request):
    logout(request)
    return render(request, 'index.html')