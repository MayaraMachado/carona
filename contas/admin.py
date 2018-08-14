# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Usuario, Telefone
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):
    add_form = UserAdminForm
    add_fieldsets =(
        (None, {
            'fields':('username', 'email', 'password1', 'password2')
        }),
        
    )
    form = UserCreationForm
    fieldsets = (
        (None, {
            'fields' : ('username', 'email')
        }),
        ('Informações Básicas', {
            'fields':('nome', 'sobrenome', 'cpf')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups','user_permissions'
                )
            }
        ),
    )
    list_filter = []
    list_display = ['username', 'nome','sobrenome', 'email', 'cpf']


admin.site.register(Usuario)
admin.site.register(Telefone)