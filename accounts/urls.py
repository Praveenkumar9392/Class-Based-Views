from django.urls import path,include
from rest_framework.routers import DefaultRouter
from accounts.views import *
from . import views
from .views import *
router = DefaultRouter()


urlpatterns = [
    path('',include(router.urls)),
    path('validate_mobile/',views.validate_mobile,name = 'validate_mobile'),
    path('verify_otp/',views.verify_otp,name = 'verify_otp'),
    path('api/login/', login),
]