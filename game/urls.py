from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_menu, name='game'),
    path("play/", views.play_mode, name='play'),
    # path("play/api/question/", views.get_question, name="get_question"),
]