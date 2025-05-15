from django.urls import path,include
from rest_framework.routers import DefaultRouter
from.import views
from catlog.views import*
router = DefaultRouter()
router.register('seo-urls', SeoUrlViewset, basename='SeoUrlViewset')

urlpatterns=[

     path('',include(router.urls)),
     path('seo-url/<str:keyword>/',seo_url,name = 'seo-url'),
]