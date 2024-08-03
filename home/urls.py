from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('saveinfo/', views.saveinfo, name='saveinfo'),
    path('index/', views.index, name='index'),
    path('<int:id>/formupdate/', views.formupdate, name='formupdate'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search',views.search,name='search'),
    
]