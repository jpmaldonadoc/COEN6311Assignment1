from django.urls import path

from ConferenceManager import views

urlpatterns = [

    path('home', views.home, name="home"),
    path('agenda', views.Agenda, name="Agenda"),
    path('homepage', views.homepage, name="homepage"),
]