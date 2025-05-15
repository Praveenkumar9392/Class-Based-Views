from django.urls import path,include
from rest_framework.routers import DefaultRouter
from.import views
from user_data.views import UserViewset
router = DefaultRouter()

router.register('users', UserViewset, basename='User')

urlpatterns=[

     path('',include(router.urls)),
]