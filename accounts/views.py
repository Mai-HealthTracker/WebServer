from django.shortcuts import render,redirect, reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User , auth 
from .models import UserData
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


# Create your views here.

@csrf_exempt
def login(request):
    if request.method=="POST":
        username = request.GET['email'] 
        password = request.GET['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            
            return JsonResponse({'message':"Account logged in successfully",'success':True,'user':request.user.username})
        else:
            return JsonResponse({'message':"Invalid Credentials",'success':False})     
    else:    
        format_dict = {'email':'Email ID','password':'Password'}
        return JsonResponse({'Request':'POST','data':format_dict})  

@csrf_exempt
def register(request):
    if request.method == "POST":
        name = request.GET["name"]
        email = request.GET["email_id"]
        gender = request.GET["gender"] 
        device_token = request.GET["device_token"]
        password1 = request.GET["password1"] 
        password2 = request.GET["password2"]

        if password1==password2:
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':"Account associated with this email already exists",'success':False})
            else:    
                user = User.objects.create_user(first_name=name,password=password1, username=email)
                user.save()
                
                auth.login(request,user)
                print(request.user)
                newUserData = UserData(name=name,email_id = email,gender = gender,device_token = device_token) 
                newUserData.save()
                return JsonResponse({'message':"Account created successfully",'success':True})
        else:
            return JsonResponse({'message':"Passwords doesn't match",'success':False})
    else:
        format_dict = {'name':'Name','email_id':'Email ID','gender':"Gender",'device_token':"Device Token"}
        return JsonResponse({'Request':'POST','data':format_dict})

@csrf_exempt
def logout(request):
    auth.logout(request)
    return JsonResponse({'message':"Logged out",'success':True})

def getaccount(request):
    userdata = request.user
    print(userdata)
    if userdata.is_anonymous:
        return JsonResponse({'message':"No Account Logged in",'status':False})
    return JsonResponse({'id':userdata.id,'name':userdata.username,'email':userdata.email,'status':True})
    # return JsonResponse(serializers.serialize("json", [userdata,]),safe = False)