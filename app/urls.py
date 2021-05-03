# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path(r'add_notification', views.UploadNotification, name='add_notification'),
    path(r'view_notification', views.ViewNotification, name='view_notification'),
    path(r'view_notes', views.ViewNotes, name='view_notes'),
    path(r'view_qps', views.ViewQps, name='view_qps'),
    path(r'add_subject', views.AddSubject, name='add_subject'),
    path(r'add_note', views.AddNotes, name='add_note'),
    path(r'add_qp', views.AddQp, name='add_qp'),
    path(r'add_assignment', views.AddAssignment, name='add_assignment'),


    # Matches any html file
   #re_path(r'^.*\.*', views.pages, name='pages'),

]

