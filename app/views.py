# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from authentication.models import User
from .forms import UploadNotificationForm
from .models import Notification

@login_required(login_url="/login/")
def index(request):
    students = User.objects.filter(is_student=True)

    context = {'students': students, 'segment': 'index'}

    if request.user.is_teacher:
        html_template = loader.get_template( 'teacher/dashboard.html')
        return HttpResponse(html_template.render(context, request))
    else:
        html_template = loader.get_template( 'student/dashboard.html')
        return HttpResponse(html_template.render(context, request))

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


@login_required(login_url="/login/")
def UploadNotification(request):
    success = False
    notification = Notification.objects.all()


    msg = "error while uploading Notice!"
    if request.method == 'POST':
        form = UploadNotificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = UploadNotificationForm()
            return render(request, 'teacher/add_notification.html', {
                'form': form,
                'notif': notification,
            })
    else:
        form = UploadNotificationForm()
    return render(request, 'teacher/add_notification.html', {
        'form': form,
        'msg': msg,
        'notif': notification
    })




