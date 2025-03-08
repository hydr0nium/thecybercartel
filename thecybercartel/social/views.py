## This are the views / the logic of the sites

from django.http import HttpResponse, HttpResponseRedirect



def login(request):
  return HttpResponse("THis is the login page")


def profile(request):
  return HttpResponse("This is the profile page!")

def shop(request):
  return HttpResponse("This is the shop page!")

def settings(request):
  return HttpResponse("This is the settings page!")

def index(request):
  return HttpResponseRedirect("login")