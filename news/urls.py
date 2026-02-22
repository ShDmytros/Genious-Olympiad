from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news'),
    path('<str:text_slug>/', views.news_detail, name='read_news'),
]