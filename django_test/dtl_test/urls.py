from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('home', views.available_students, name='available_students'),
]