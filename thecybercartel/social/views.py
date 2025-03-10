## This are the views / the logic of the sites

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from social.database_manager import create_user, login_user
from django.views.generic import TemplateView


def logout(request):
  request.session["authenticated"] = False
  request.session["username"] = "" 
  return HttpResponseRedirect("login")

  
class LoginView(TemplateView):

  def get(self, request: HttpRequest, *args, **kwargs):
    if "authenticated" in request.session and request.session['authenticated']:
      return HttpResponseRedirect("/")
    return render(request, "login.html", {})

  def post(self, request: HttpRequest, *args, **kwargs):
    params = ["username", "password"]
    if not all(param in request.POST for param in params):
      return HttpResponse(status=204)
    username = request.POST["username"]
    password = request.POST["password"]
    if login_user(username, password):
      request.session["authenticated"] = True
      request.session["username"] = username 
      return HttpResponseRedirect("/")
    return render(request, "login.html", {"error": True, "message": "Wrong username or password"})


  
class RegisterView(TemplateView):

  def get(self, request: HttpRequest, *args, **kwargs):
    if "authenticated" in request.session and request.session['authenticated']:
      return HttpResponseRedirect("/")
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
      return HttpResponseRedirect("/")
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
  return render(request, "index.html", {"username": request.session["username"]})

