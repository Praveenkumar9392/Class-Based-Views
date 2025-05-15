from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Blogcategory, Blog, Contacts,Bookings
from .serializers import BlogcategorySerializer,BlogSerializer,CreateBlogSerializer,CreateBlogcategorySerializer,ContactsSerializer,BookingsSerializer
from catlog.models import SeoUrl
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from masters.user_mixin import UserTrackingMixin,DeleteMixin

class CustomPagination(PageNumberPagination):
    from django.conf import settings
    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
    page_size_query_param = 'page_size'
    max_page_size = 10000000


class BlogcategoryViewSet(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = Blogcategory.objects.all()
    pagination_class = CustomPagination
    serializer_class = BlogcategorySerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['id', 'title', 'is_active', 'image', 'sort']
    filterset_fields = ['is_suspended'] 
    
    def get_serializer_class(self):
        if self.request.method  != 'GET':
            return CreateBlogcategorySerializer
        return BlogcategorySerializer
    
    def create(self, request, *args, **kwargs):
        keyword = request.data.get('slug')
        if not keyword:
            return Response({"error": "Slug is required."}, status=status.HTTP_400_BAD_REQUEST)

        if SeoUrl.objects.filter(keyword=keyword).exists():
            return Response({"error": "A Blogcategory with this slug already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blogcategory_obj = serializer.save(cuser=self.request.user )
        content_type = ContentType.objects.get_for_model(Blogcategory)
        seo_obj = SeoUrl.objects.create(
            content_type=content_type,
            object_id=blogcategory_obj.pk,
            content_object=blogcategory_obj,
            keyword=keyword,
            cuser = self.request.user
               
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        keyword = request.data.get('slug')
        if not keyword:
            return Response({"error": "Slug is required."}, status=status.HTTP_400_BAD_REQUEST)

        if SeoUrl.objects.filter(keyword=keyword).exclude(object_id=instance.pk).exists():
            return Response({"error": "A Blogcategory with this slug already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        blogcategory_obj = serializer.save(muser=self.request.user)

        seo_obj = SeoUrl.objects.get(content_type__model='blogcategory', object_id=blogcategory_obj.pk)
        seo_obj.keyword = keyword
        seo_obj.muser=self.request.user
        seo_obj.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


    
class BlogViewSet(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['id','keywords','meta_description','title','content','image','is_active','sort']
    filterset_fields = ['category','is_suspended']

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return CreateBlogSerializer
        return BlogSerializer
    
    def create(self, request, *args, **kwargs):
        category_id = request.data.get('category')
        if not category_id:
            return Response({"error": "Category is required."}, status=status.HTTP_400_BAD_REQUEST)

        if Blogcategory.objects.filter(id=category_id, is_suspended=True).exists():
            return Response({"error": "Selected blog category is suspended."}, status=status.HTTP_400_BAD_REQUEST)

        keyword = request.data.get('slug')
        if not keyword:
            return Response({"error": "Slug is required."}, status=status.HTTP_400_BAD_REQUEST)

        if SeoUrl.objects.filter(keyword=keyword).exists():
            return Response({"error": "A Blogcategory with this slug already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog_obj = serializer.save(category_id=category_id,cuser=self.request.user)
        content_type = ContentType.objects.get_for_model(Blog)
        seo_obj = SeoUrl.objects.create(
            content_type=content_type,
            object_id=blog_obj.pk,
            content_object=blog_obj,
            keyword=keyword,
            cuser = self.request.user
               
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        category_id = request.data.get('category')
        print(category_id,'category_id')
        if not category_id:
            return Response({"error": "Category is required."}, status=status.HTTP_400_BAD_REQUEST)

        if Blogcategory.objects.filter(id=category_id, is_suspended=True).exists():
            return Response({"error": "Selected blog category is suspended."}, status=status.HTTP_400_BAD_REQUEST)

        keyword = request.data.get('slug')
        if not keyword:
            return Response({"error": "Slug is required."}, status=status.HTTP_400_BAD_REQUEST)

        if SeoUrl.objects.filter(keyword=keyword).exclude(object_id=instance.pk).exists():
            return Response({"error": "A Blogcategory with this slug already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        print(serializer,'serializer')
        serializer.is_valid(raise_exception=True)
        blog_obj = serializer.save(category_id=category_id,muser=self.request.user)
        seo_obj = SeoUrl.objects.get(content_type__model='blog', object_id=blog_obj.pk)
        seo_obj.keyword = keyword
        seo_obj.muser = self.request.user
        seo_obj.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ContactsViewSet(DeleteMixin,viewsets.ModelViewSet):
    queryset = Contacts.objects.all().order_by('-id')
    serializer_class = ContactsSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name','email']
    filterset_fields = ['is_suspended'] 
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny] 

class BookingsViewSet(DeleteMixin,viewsets.ModelViewSet):
    queryset = Bookings.objects.all().order_by('-id')
    serializer_class = BookingsSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['full_name','email']
    filterset_fields = ['is_suspended'] 
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny] 