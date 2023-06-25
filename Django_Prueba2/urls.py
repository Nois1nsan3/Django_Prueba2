"""Django_Prueba2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Prueba2Django.views import seminario_add, seminario_delete, seminario_list, seminario_mod, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('lista/', seminario_list, name='lista'),
    path('agregar/', seminario_add),
    path('modificar/<int:id>/', seminario_mod, name='modificar'),
    path('eliminar/<int:id>/', seminario_delete, name='eliminar'),
]
