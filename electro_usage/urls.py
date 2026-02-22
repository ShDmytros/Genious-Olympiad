from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='electro_usage'),
]