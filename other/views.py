from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


def simple_view(request):
    return HttpResponse('Hello!! Love u sexy and Team Bom Bom!!')

# Create your views here.

class AboutView(TemplateView):
    template_name = 'other/about.html'

class ExtraView(TemplateView):
    template_name = 'other/extra.html'