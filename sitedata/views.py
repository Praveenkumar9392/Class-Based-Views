from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from masters.user_mixin import UserTrackingMixin,DeleteMixin

class CustomPagination(PageNumberPagination):
    from django.conf import settings
    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
    page_size_query_param = 'page_size'
    max_page_size = 10000000
    
     
from .sitemap_views import index, sitemap as get_sitemap
from sitedata.sitemap import  BlogSitemap, BlogcategorySitemap, InformationPageSitemap,AdditionalSitemapUrlSitemap

sitemaps = {
    'blog': BlogSitemap,
    'blogcategory': BlogcategorySitemap,
    'informationpage': InformationPageSitemap,
    'AdditionalSitemapUrl':AdditionalSitemapUrlSitemap
}
def sitemap_index(request):
    return index(request,sitemaps)

def sitemap(request,section):
    return get_sitemap(request,sitemaps,section)