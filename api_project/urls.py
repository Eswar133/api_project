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
    path('api/banks', views.BankAPIView.as_view(), name='create-bank'),
    path('api/banks', views.BankAPIView.as_view(), name='get-banks'),
    path('api/branch', views.BranchAPIView.as_view(), name='create-branch'),
    path('api/branch/<str:ifsc>/', views.BranchAPIView.as_view(), name='get-branch'),
    path('banks/', views.banks_view, name='banks'),
    path('branches/', views.branches_view, name='branches_view'),
    
]

