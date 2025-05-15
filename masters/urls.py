from django.urls import path,include
from rest_framework.routers import DefaultRouter
from masters.views import *
router = DefaultRouter()

router.register('countries',CountryViewset,basename='Country')
router.register('states',StateViewset,basename='State')
router.register('cities',CityOrTownViewset,basename='City')
router.register('areas',AreaViewset,basename='Area')

urlpatterns=[

     path('',include(router.urls)),
     path('import/',import_data_from_json, name='import_data_from_json'),
]