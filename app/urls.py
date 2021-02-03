# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from app import views

urlpatterns = [

    # The home page
    #path('', views.index, name='home'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),
    path('i18n/', include('django.conf.urls.i18n')),  # Make sure this is present or the set_language url will not be found

]



