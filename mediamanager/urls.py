from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaFolderViewSet,MediaItemViewSet

router = DefaultRouter()
router.register('media-folders', MediaFolderViewSet,basename="MediaFolderViewSet")
router.register('media-items', MediaItemViewSet,basename="MediaItemViewSet")

urlpatterns = [
    path('', include(router.urls)),
]

