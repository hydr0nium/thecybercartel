## This are the views / the logic of the sites

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template




def login(request):
  return HttpResponse("This is the login page")


def profile(request):
  if "authenticated" not in request.session or not request.session['authenticated']:
    return HttpResponseRedirect("login")


  return HttpResponse("This is the profile page!")

def shop(request):
  if "authenticated" not in request.session or not request.session['authenticated']:
    return HttpResponseRedirect("login")
  return HttpResponse("This is the shop page!")

def settings(request):
  if "authenticated" not in request.session or not request.session['authenticated']:
    return HttpResponseRedirect("login")
  return HttpResponse("This is the settings page!")

def index(request):
  if "authenticated" not in request.session or not request.session['authenticated']:
    return HttpResponseRedirect("login")

def test(request):
  request.session["authenticated"] = True
  return HttpResponse("you are logged in now!")
