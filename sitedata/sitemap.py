from django.contrib.sitemaps import Sitemap
from blogapp.models import Blog,Blogcategory
from catlog.models import *

   
class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    limit = 100

    def items(self):
        return Blog.objects.order_by('sort')
    
    def lastmod(self, obj):
        return obj.mdate
    
    def location(self, obj):
        return f'/{obj.get_slug()}' 

class BlogcategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    limit = 100

    def items(self):
        return Blogcategory.objects.order_by('sort')

    def lastmod(self, obj):
        return obj.mdate
    
    def location(self, obj):
        return f'/{obj.get_slug()}' 

class InformationPageSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    limit = 100

    def items(self):
        return InformationPage.objects.order_by('sort')

    def lastmod(self, obj):
        return obj.mdate
    
    def location(self, obj):
        return f'/{obj.get_slug()}'
    
class AdditionalSitemapUrlSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    limit = 100

    def items(self):
        return AdditionalSitemapUrl.objects.all()

    def lastmod(self, obj):
        return obj.mdate
    
    def location(self, obj):
        return f'/{obj.slug}'