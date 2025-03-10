## This are the views / the logic of the sites

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from social.database_manager import create_user
from django.views.generic import TemplateView
from django.template import Context


def logout(request):
  pass

class LoginView(TemplateView):

  def get(self, request: HttpRequest, *args, **kwargs):
    if "authenticated" in request.session and request.session['authenticated']:
      return HttpResponseRedirect("index")
    return render(request, "index.html", {})

  def post(self, request: HttpRequest, *args, **kwargs):
    pass

class RegisterView(TemplateView):

  def get(self, request: HttpRequest, *args, **kwargs):
    if "authenticated" in request.session and request.session['authenticated']:
      return HttpResponseRedirect("index")
    return render(request, "register.html", {})


  def post(self, request: HttpRequest, *args, **kwargs):
    params = ["username", "password"]
    if not all(param in request.POST for param in params):
      return HttpResponse(status=204)
    username = request.POST["username"]
    password = request.POST["password"]
    if create_user(username=username, password=password):
      request.session["authenticated"] = True
      request.session["username"] = username 
      return render(request, "index.html", {})
    else:
      return render(request, "register.html", {"error": True, "message": "User already exists"})
    
    


def profile(request: HttpRequest):
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

