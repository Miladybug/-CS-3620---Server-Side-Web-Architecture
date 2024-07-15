from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Hobby
from .models import Portfolio

# Create your views here.
def home(request):
    return HttpResponse("Hello! I'm Emma Johnson. Welcome to my portfolio")

def hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)

def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)

def contact(request):
    return HttpResponse("Contact me at emmajohnson@mail.weber.edu")
