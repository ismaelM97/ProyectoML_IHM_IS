from django.shortcuts import render

# Create your views here.

def home(request,*args, **kwargs):
    return render(request,'index.html',{})

def base(request,*args, **kwargs):
    return render(request, 'home.html',{})


def about(request,*args, **kwargs):
    return render(request, 'about.html',{})

def servicio(request,*args, **kwargs):
    return render(request, 'services.html',{})

def department(request,*args, **kwargs):
    return render(request, 'departments.html',{})


def doctor(request,*args, **kwargs):
    return render(request, 'doctors.html',{})
    

def contact(request,*args, **kwargs):
    return render(request, 'contact.html',{})

def register(request,*args, **kwargs):
    return render(request, 'register.html',{})