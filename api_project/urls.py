"""
URL configuration for banks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bank import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create_bank/', views.create_bank, name='create-bank'),
    path('api/get_banks/', views.get_banks, name='get-banks'),
    path('api/create_branch/', views.create_branch, name='create-branch'),
    path('api/get_branch/', views.get_branch, name='get-branch'),
    path('banks/', views.banks_view, name='banks'),
    path('branches/', views.branches_view, name='branches_view'),
]

