# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView




class TrajetoView(TemplateView):
    template_name = "trajeto.html"
    

class ViagemView(TemplateView):
    template_name = "trajeto.html"
    context = {}
    context['id'] = 1
