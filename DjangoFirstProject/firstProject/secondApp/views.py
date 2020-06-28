from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_morning(request):
    return HttpResponse("<b>Good Morning Dears</b></br><a href='http://127.0.0.1:8000/hellopage/'>Go Back</a>")

def good_evening(request):
    return HttpResponse("<b>Good Evening Dears</b></br><a href='http://127.0.0.1:8000/hellopage/'>Go Back</a>")

def good_afternoon(request):
    return HttpResponse("<b>Good Afternoon Dears</b></br><a href='http://127.0.0.1:8000/hellopage/'>Go Back</a>")
