from django.urls import path
from .import views

urlpatterns = [
    path('',views.simple_view)
    path('about/',AboutPage.as_view(),name='about')
]

