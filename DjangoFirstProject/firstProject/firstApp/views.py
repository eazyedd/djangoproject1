from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s='<h1>Hello Friends, Durga sir is great!</h1>\n'
    gm ="<a href='http://127.0.0.1:8000/gm/'>Wish Good Morning</a></br>"
    ga ="<a href='http://127.0.0.1:8000/ga/'>Wish Good Afternoon</a></br>"
    ge ="<a href='http://127.0.0.1:8000/ge/'>Wish Good Evening</a></br>"
    return HttpResponse(s+gm+ga+ge)
