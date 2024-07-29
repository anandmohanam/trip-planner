from __future__ import unicode_literals

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from myapp.forms import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import *
import sqlite3


def index(request):
    packages = Package.objects.all()
    context = {'packages':packages}
    return render(request, 'index.html', context)


def packages(request):
    packages = Package.objects.all()
    context = {'packages':packages}
    return render(request, 'package.html', context)


def package_details(request,pk):
    package = Package.objects.get(id=pk)
    menus = Menu.objects.filter(package=package)
    context = {'package':package,'menus':menus}
    return render(request, 'package_details.html', context)


def payment(request):
    context = {}
    return render(request, 'payment.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html',context)


def register(request):
    print('form one')
    form = CreateUserForm()
    if request.POST:
        print('form two')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account created for '+ form.cleaned_data.get('username'))
            return redirect('login')
        else:
            messages.error(request, 'invalid form')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_view(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('index')
        else:
            messages.error(request, 'invalid credentials')
    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')







def contact1(request):
    data=contactus(request.GET)
    if data.is_valid():
        fullname = data.cleaned_data['fullname']
        Email = data.cleaned_data['Email']
        msg = data.cleaned_data['msg']

        e=Contact(fullname=fullname,Email=Email,msg=msg)
       
        e.save()
    return render(request, 'contact.html', {})
