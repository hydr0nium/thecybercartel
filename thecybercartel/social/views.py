## This are the views / the logic of the sites

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template




def login(request):
  return HttpResponseRedirect("testlogin")


def profile(request):
  if "authenticated" not in request.session or not request.session['authenticated']:
    return HttpResponseRedirect("login")
  return render(request, "profile.html", {})

def shop(request):
  if "authenticated" not in request.session or not request.session['authenticated']:
    return HttpResponseRedirect("login")
  return render(request, "shop.html", {})

def settings(request):
  if "authenticated" not in request.session or not request.session['authenticated']:
    return HttpResponseRedirect("login")
  return render(request, "settings.html", {})

def index(request):
  if "authenticated" not in request.session or not request.session['authenticated']:
    return HttpResponseRedirect("login")
  return render(request, "index.html", {})

def testlogin(request):
  request.session["authenticated"] = True
  return HttpResponse("you are logged in now!")
