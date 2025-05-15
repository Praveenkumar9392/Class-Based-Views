"""construction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from sitedata.views import sitemap_index, sitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("accounts.urls")),
    path('catlog/',include('catlog.urls')),
    # path('stores/',include('stores.urls')),
    path('masters/',include('masters.urls')),
    # path('cms/',include("cms.urls")),
    path('blogapp/',include('blogapp.urls')),
    path('mediamanager/',include('mediamanager.urls')),
    # path('client_management/',include('client_management.urls')),
    path('careers/',include('careers.urls')),
    # path('central/',include('central.urls')),
    path('sitedata/',include('sitedata.urls')),
    path('user_data/',include('user_data.urls')),
    # path('deliveryagent/',include('deliveryagent.urls')),
    path('sitemap.xml', sitemap_index, name='sitemap-index'),
    path('sitemap/<section>.xml', sitemap, name='django.contrib.sitemaps.views.sitemap'),
    # path("subscription/",include("subscription.urls")),
    path('message_framework/',include('message_framework.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
