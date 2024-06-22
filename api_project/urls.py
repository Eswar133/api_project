from django.contrib import admin
from django.urls import path
from bank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_bank/', views.create_bank, name='create_bank'),
    path('get_bank/<int:bank_id>/', views.get_bank, name='get_bank'),
    path('create_branch/', views.create_branch, name='create_branch'),
    path('get_branch/', views.get_branch, name='get_branch'),
    path('get_branch/<str:ifsc>/', views.get_branch, name='get_branch_ifsc'),
 
]
