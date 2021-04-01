# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)
    code = "staff@soecusat"
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_teacher:
                    staff_code = form.cleaned_data.get("staff_code")
                    print(staff_code)
                    if code == staff_code:
                        login(request, user)
                        return redirect("/")
                    elif staff_code == "":
                        msg = "Please enter the staff code!"
                        return render(request, "accounts/login.html", {"form": form, "msg" : msg})
                    else:
                        msg = "Wrong staff code!"
                        return render(request, "accounts/login.html", {"form": form, "msg" : msg})
                else:
                    pass
                login(request, user)
                request.user.save()
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})


def register_user(request):

    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            mode = form.cleaned_data.get("mode")
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            # selected_mode = form.cleaned_data["mode"]
            # request.session['selected_mode'] = selected_mode
            # user = authenticate(username=username, password=raw_password,)
            user = form.save()
            print(mode)
            login(request, user)
            if mode == "Student" and request.user.is_student == False:
                request.user.is_student = True
                request.user.save()
                print("student ok")

            elif mode == "Teacher" and request.user.is_teacher == False:
                request.user.is_teacher = True
                request.user.save()
                print("teacher ok")

            else:
                print("Error on assigning roles")

            #debug
            print("register model")
            print(mode)
            logout(request)
            msg = 'User created - please <a href="/login">login</a>.'
            success = True
            
            # return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
