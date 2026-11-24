from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('dashboard/',views.DashboardView.as_view(),name="dashboard"),
]
