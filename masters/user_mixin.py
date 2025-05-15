from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from blogapp.models import Blog,Blogcategory
from collections.abc import Iterable
class UserTrackingMixin:
    def perform_create(self, serializer):
        serializer.save(cuser=self.request.user)

    def perform_update(self, serializer):
        serializer.save(muser=self.request.user)
class DeleteMixin:
    def destroy(self, request, *args, **kwargs):
        queryset = self.get_object()
        queryset.is_suspended = True
        queryset.save()
        model_name = queryset._meta.model.__name__
        if model_name in ['DiscountCoupon', 'BogoDiscount']:
            queryset.coupon.is_suspended = True
            queryset.coupon.save()
        elif model_name == 'Blogcategory':
            related_blogs = Blog.objects.filter(category=queryset)
            for blog in related_blogs:
                blog.is_suspended = True
                blog.save()
        return Response(data='Delete success')
    
    @action(detail=True, methods=['POST'])
    def revive(self, request, *args, **kwargs):
        queryset = self.get_object()
        queryset.is_suspended = False
        queryset.save()
        model_name = queryset._meta.model.__name__
        if model_name == 'DiscountCoupon':
            queryset.coupon.is_suspended = False
            queryset.coupon.save()
        elif model_name == 'Blogcategory':
            related_blogs = Blog.objects.filter(category=queryset)
            for blog in related_blogs:
                blog.is_suspended = False
                blog.save()
        return Response(data='Revive success')