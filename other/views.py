from django.shortcuts import render
from django.http import HttpResponse

def simple_view(request):
    return HttpResponse('Hello James')

# Create your views here.
