from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogcategoryViewSet, BlogViewSet ,ContactsViewSet,BookingsViewSet

router = DefaultRouter()
router.register('blogcategory', BlogcategoryViewSet,basename="blogcategory")
router.register('blog', BlogViewSet,basename="blog")
router.register('contacts', ContactsViewSet,basename="contacts")
router.register('bookings', BookingsViewSet,basename="bookings")

urlpatterns = [
    path('', include(router.urls)),
]

