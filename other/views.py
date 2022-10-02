from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def simple_view(request):
    return HttpResponse('Hello Sexy!! Love u sexy and Team Bom Bom!!')

# Create your views here.

class AboutPage(TemplateView):
    template_name = "about.html"