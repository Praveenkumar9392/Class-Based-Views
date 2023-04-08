"""crudcbv3 URL Configuration

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
from testapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', companylist.as_view(),name='companies'),
    path('<int:pk>/', companydetail.as_view(),name='detail'),
    path('create/', companycreateview.as_view()),
    path('update/<int:pk>/', companyupdateview.as_view()),
    path('delete/<int:pk>/', companydeleteview.as_view()),

]
