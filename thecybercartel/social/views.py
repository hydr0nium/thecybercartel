## This are the views / the logic of the sites

from django.http import HttpResponse



def login(request):
  return HttpResponse("This is the login page!")


def profile(request):
  return HttpResponse("This is the profile page!")