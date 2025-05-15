from django.shortcuts import render
from rest_framework import viewsets
from user_data.models import User
from user_data.serializers import UserSerializer,CreateuserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from accounts.views import CustomPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from masters.user_mixin import UserTrackingMixin,DeleteMixin

class UserViewset(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['is_suspended']  
    pagination_class = CustomPagination
    search_fields = ['name','meta_title','is_suspended']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method  != 'GET':
            return CreateuserSerializer
        return UserSerializer 