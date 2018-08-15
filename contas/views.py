# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Usuario
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import UserAdminForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



def site_logout(request):
    logout(request)
    return redirect('index.html')


class RegisterView(CreateView):
    model = Usuario
    template_name = 'cadastro-usuario.html'
    form_class = UserAdminForm
    success_url = reverse_lazy('index')
    

class UserDetailsListView(LoginRequiredMixin, ListView):
    model = Usuario
    context_object_name = 'Usuario'
    template_name = 'profile.html'