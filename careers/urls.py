from django.urls import path, include
from rest_framework import routers
from .views import JobCategoryViewSet, JobListingViewSet, JobApplicationViewSet


router = routers.DefaultRouter()
router.register('job-posts', JobListingViewSet,basename="JobListing")
router.register('job-applications', JobApplicationViewSet,basename="JobApplication")
router.register('job-categories', JobCategoryViewSet,basename="JobCategory")
urlpatterns = [
    path('', include(router.urls)),
]
