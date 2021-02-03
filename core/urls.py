# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),          # UI Kits Html files
    path("", include("politico.urls")),  # Routes for politico

)
