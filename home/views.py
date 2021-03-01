from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User , auth 

# Create your views here.

def home(request):
    return HttpResponse(User.objects.get(username = 'darani').email)