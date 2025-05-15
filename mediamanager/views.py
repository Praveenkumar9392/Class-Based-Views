from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import MediaFolder,MediaItem
from .serializers import MediaFolderSerializer,MediaItemSerializer,CreateMediaItemSerializer
from catlog.models import SeoUrl
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from masters.user_mixin import UserTrackingMixin,DeleteMixin

class CustomPagination(PageNumberPagination):
    from django.conf import settings
    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
    page_size_query_param = 'page_size'
    max_page_size = 500


class MediaFolderViewSet(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = MediaFolder.objects.all()
    serializer_class = MediaFolderSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['id','name',]
    filterset_fields = ['parent_folder','is_suspended']

    def get_queryset(self):
        queryset = super().get_queryset()
        is_root = self.request.query_params.get('is_root', '').lower()
        if is_root == 'true':
            queryset = queryset.filter(parent_folder__isnull=True)
        return queryset

class MediaItemViewSet(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['id','name','image']
    filterset_fields = ['folder','is_trash','is_suspended']

    def get_queryset(self):
        queryset = super().get_queryset()
        is_root = self.request.query_params.get('is_root', '').lower()
        if is_root == 'true':
            queryset = queryset.filter(folder__isnull=True)
        return queryset
    
    def get_serializer_class(self):
        if self.request.method != "GET":
            return CreateMediaItemSerializer
        return MediaItemSerializer
    
    def create(self, request, *args, **kwargs):
        image_list = request.data.getlist('image',[])
        folder = request.data.get('folder',None)
        if folder == 'null':
            folder = None

        # if folder and folder.is_suspended:
        #     return Response(f"Selected folder is suspended.", status=status.HTTP_400_BAD_REQUEST)
        
        for image_data in image_list:
            MediaItem.objects.create(folder_id=folder, image=image_data,cuser=self.request.user)

        return Response("Successfully uploaded", status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['PUT'])
    def move_to_trash(self, request):
        media_item_ids = request.data.get('media_item_ids', [])
        print(media_item_ids,'media_item_ids')

        for media_item_id in media_item_ids:
            try:
                media_item = MediaItem.objects.get(id=media_item_id)
                print(media_item.id,'media_item')
                media_item.folder = None
                media_item.is_trash = True
                media_item.muser = self.request.user
                media_item.save()
            except MediaItem.DoesNotExist:
                return Response({"error": "MediaItem with ID {} does not exist.".format(media_item_id)}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Media items moved to trash successfully"})