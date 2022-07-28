from django.shortcuts import render,HttpResponse
from ConferenceManager.models import Event
from django.template import Template,Context
# Create your views here.

def homepage(request):
    return render(request, "ConferenceManager/homepage.html")

def Agenda(request):

    Agenda=Event.objects.all()
    return render(request, "ConferenceManager/Agenda.html", {"Agenda": Agenda})

def Test(request):
    return render(request, "ConferenceManager/Test.html")

def home(request):
       return render (request, "ConferenceManager/home.html")



