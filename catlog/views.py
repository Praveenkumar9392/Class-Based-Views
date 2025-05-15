from rest_framework import viewsets
from catlog.models import *
from catlog.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from masters.user_mixin import UserTrackingMixin,DeleteMixin
from user_data.models import User  
from django.shortcuts import get_object_or_404
from blogapp.models import Blog,Blogcategory
from blogapp.serializers import BlogcategorySerializer,BlogSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    from django.conf import settings
    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
    page_size_query_param = 'page_size'
    max_page_size = 10000000

class SeoUrlViewset(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = SeoUrl.objects.all()
    serializer_class = SeoUrlSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['keyword','is_suspended']


@api_view(['GET'])
def seo_url(request,keyword):
    status_code = status.HTTP_200_OK
    message = {"product_type":"","product_data":""}
    try:
        seo_obj = SeoUrl.objects.get(keyword=keyword,  )
        if seo_obj.content_type.model == "blog":
            obj = Blog.objects.get(pk=seo_obj.object_id)
            message['product_type'] = "blog"
            message['product_data'] = BlogSerializer(obj,many=False).data
        if seo_obj.content_type.model == "blogcategory":
            obj = Blogcategory.objects.get(pk=seo_obj.object_id)
            message['product_type'] = "blogcategory"
            message['product_data'] = BlogcategorySerializer(obj,many=False).data
    except:
        message = "SeoUrl matching query does not exist."
        status_code = status.HTTP_400_BAD_REQUEST
    return Response(message,status_code)