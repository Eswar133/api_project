from django.contrib import admin
from django.urls import path
from bank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_bank/', views.create_bank, name='create_bank'),
    path('get_bank/<int:bank_id>/', views.get_bank, name='get_bank'),
]
