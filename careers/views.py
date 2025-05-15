from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import JobCategory, JobListing, JobApplication
from rest_framework.pagination import PageNumberPagination
from .serializers import JobCategorySerializer, JobListingSerializer, JobApplicationSerializer, CreateJobApplicationSerializer, CreateJobListingSerializer,CreateJobCategorySerializer
from masters.user_mixin import UserTrackingMixin,DeleteMixin

class CustomPagination(PageNumberPagination):
    from django.conf import settings
    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
    page_size_query_param = 'page_size'
    max_page_size = 10000000

class JobCategoryViewSet(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['category']
    filterset_fields = ['is_suspended']

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return CreateJobCategorySerializer
        return JobCategorySerializer



class JobListingViewSet(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['job_id', 'title', 'category']
    filterset_fields = ['is_suspended','category']

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return CreateJobListingSerializer
        return JobListingSerializer

class JobApplicationViewSet(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    pagination_class = CustomPagination
    serializer_class = JobApplicationSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['job', 'full_name', 'email']
    filterset_fields = ['is_suspended','job']

    
    def get_serializer_class(self):
        if self.request.method != 'GET':
            return CreateJobApplicationSerializer
        return JobApplicationSerializer