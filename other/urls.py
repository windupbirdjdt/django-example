from django.urls import path
from . import views 
from .views import AboutView, ExtraView

urlpatterns = [
    path('',views.simple_view),
   path('about/',AboutView.as_view(),name='about'),
   path('extra/',ExtraView.as_view(),name='extra')
]

