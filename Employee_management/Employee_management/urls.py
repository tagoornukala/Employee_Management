"""Employee_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from employees import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_employee/',views.create_employee,name='create_employee'),
    path('edit_employee/<int:employee_id>/',views.edit_employee,name='edit_employee'),
    path('delete_employee/<int:employee_id>/',views.delete_employee, name='delete_employee'),
    path('',views.employee_list, name='employee_list'),
]
