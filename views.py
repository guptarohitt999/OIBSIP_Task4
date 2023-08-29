from django.http import HttpResponse
from django.shortcuts import render,redirect
from service.models import Employee
from service.models import signup
from service.backend import logins,logouts
from django.contrib.auth import authenticate, login
from django.contrib import sessions

def employee(request):
    if request.method=="POST":
        n1=request.POST.get('Name')
        n2=request.POST.get('Email')
        n3=request.POST.get('Phone')
        n4=request.POST.get('Address')
        en=Employee(Name=n1,Email=n2,Phone=n3,Address=n4)
        en.save()
    data=Employee.objects.all().values()
    dic={
        'name':data
    }
    return render(request,'index.html',dic)

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        data1=signup.objects.filter(Email=email).values()
        data=list(data1)
        if data!=[]:
            dbPassword=data[0]["Password"]
            if dbPassword==password:
                logins(request,data)
                print(data[0]["Name"])
                return redirect('home')
            else:
                message="invalid email or password"
                messages={"message":message}
                return render(request,'login.html',messages)
        else:
            message="invalid email or password"
            messages={"message":message}
            return render(request,'login.html',messages)       
    return render(request,'login.html')

def signupfunc(request):
    if request.method=="POST":
        n1=request.POST.get('name')
        n2=request.POST.get('email')
        n3=request.POST.get('phone')
        n4=request.POST.get('password')
        n5=request.POST.get('gender')
        en=signup(Name=n1,Email=n2,Phone=n3,Password=n4,Gender=n5)
        en.save()
        return redirect('login')
    return render(request,'signup.html')

def logout(request):
    logouts(request)
    return redirect('userlogin')