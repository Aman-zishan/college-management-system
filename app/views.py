# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .decorators import teacher_required
from authentication.models import User
from .forms import UploadNotificationForm, AddSubjectForm, AddSubjectNotesForm, AddSubjectQpForm, AddSubjectAssignmentForm
from .models import Notification, Subject, Notes

from django.views.generic import ListView

@login_required(login_url="/login/")
def index(request):
    students = User.objects.filter(is_student=True)
    subjects = Subject.objects.all()

    context = {'students': students, 'segment': 'index', 'subjects': subjects}

    if request.user.is_teacher:
        html_template = loader.get_template( 'teacher/dashboard.html')
        return HttpResponse(html_template.render(context, request))
    else:
        html_template = loader.get_template( 'student/dashboard.html')
        return HttpResponse(html_template.render(context, request))

'''

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
'''


@login_required(login_url="/login/")
@teacher_required
def UploadNotification(request):
    msg = ""
    color = "text-danger"

    if request.method == 'POST':
        form = UploadNotificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = "Successfully added subject!"
            color = "text-success"
            form = UploadNotificationForm()
            return render(request, 'teacher/add_item.html', {
                'msg': msg,
                'form': form,
                'color': color


            })
    else:
        form = UploadNotificationForm()
    return render(request, 'teacher/add_item.html', {
        'form': form,
        'msg': msg,

    })


@login_required(login_url="/login/")
@teacher_required
def AddSubject(request):


    msg = ""
    color = "text-danger"
    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Successfully added subject!"
            color = "text-success"
            form = AddSubjectForm()
            return render(request, 'teacher/add_item.html', {
                'form': form,

                'msg': msg,
                'color': color
            })
    else:

        form = AddSubjectForm()
    return render(request, 'teacher/add_item.html', {
        'form': form,
        'msg': msg,
        'color': color,
    })

@login_required(login_url="/login/")
@teacher_required
def AddNotes(request):


    msg = ""
    color = "text-danger"
    if request.method == 'POST':
        form = AddSubjectNotesForm(request.POST, request.FILES)
        print(form.errors)
        print(request.POST.get("subject"))

        if form.is_valid():

            form.save()
            form = AddSubjectNotesForm()
            msg = "Successfully added subject notes!"
            color = "text-success"
            return render(request, 'teacher/add_item.html', {
                'form': form,
                'msg': msg,
                'color': color
            })
    else:

        form = AddSubjectNotesForm()
    return render(request, 'teacher/add_item.html', {
        'form': form,
        'msg': msg,
        'color': color,
    })


@login_required(login_url="/login/")
@teacher_required
def AddAssignment(request):

    msg = ""
    color = "text-danger"
    if request.method == 'POST':
        form = AddSubjectAssignmentForm(request.POST, request.FILES)
        print(form.errors)
        print(request.POST.get("subject"))

        if form.is_valid():

            form.save()
            form = AddSubjectAssignmentForm()
            msg = "Successfully added Assignment!"
            color = "text-success"
            return render(request, 'teacher/add_item.html', {
                'form': form,
                'msg': msg,
                'color': color
            })
    else:

        form = AddSubjectAssignmentForm()
    return render(request, 'teacher/add_item.html', {
        'form': form,
        'msg': msg,
        'color': color,
    })


@login_required(login_url="/login/")
def ViewNotification(request):
    success = False
    notification = Notification.objects.all()

    return render(request, 'student/view_notifications.html', {

                'notif': notification,
            })


@login_required(login_url="/login/")
@teacher_required
def AddQp(request):

    notes = Notes.objects.all()
    msg = ""
    color = "text-danger"
    if request.method == 'POST':
        form = AddSubjectQpForm(request.POST, request.FILES)
        print(form.errors)
        print(request.POST.get("subject"))

        if form.is_valid():

            form.save()
            form = AddSubjectQpForm()
            msg = "Successfully added subject question paper!"
            color = "text-success"
            return render(request, 'teacher/add_item.html', {
                'form': form,
                'msg': msg,
                'color': color
            })
    else:

        form = AddSubjectQpForm()
    return render(request, 'teacher/add_item.html', {
        'form': form,
        'msg': msg,
        'color': color,
    })



