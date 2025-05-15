from django.shortcuts import render
from rest_framework import viewsets,status
from masters.models import *
from masters.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404 
from django.db.models import Q
from django.db import IntegrityError
import csv
from django.http import HttpResponse
from .user_mixin import UserTrackingMixin,DeleteMixin

class CustomPagination(PageNumberPagination):
    from django.conf import settings
    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
    page_size_query_param = 'page_size'
    max_page_size = 10000000

from math import radians, sin, cos, sqrt, atan2

class CountryViewset(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = Country.objects.filter(is_deleted=False)
    serializer_class = CountrySerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['country_name']
    filterset_fields = ['is_suspended']
    pagination_class = CustomPagination

class StateViewset(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = State.objects.filter(is_deleted=False)
    serializer_class = StateSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = [ 'country__country_name', 'state_name']
    filterset_fields = ['country','is_suspended']
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.request.method != "GET":
            return CreateStateSerializer
        return StateSerializer 

class CityOrTownViewset(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = CityOrTown.objects.filter(is_deleted=False)
    serializer_class = CityOrTownSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = [ 'state__state_name', 'city_name']
    filterset_fields = ['state','is_suspended']
    pagination_class = CustomPagination 

    def get_serializer_class(self):
        if self.request.method != "GET":
            return CreateCityOrTownSerializer
        return CityOrTownSerializer   


class AreaViewset(UserTrackingMixin,DeleteMixin,viewsets.ModelViewSet):
    queryset = Area.objects.filter(is_deleted=False)
    serializer_class = AreaSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = [ 'pincode',  'name']
    filterset_fields = ['city','is_suspended','pincode']
    pagination_class = CustomPagination 

    def get_serializer_class(self):
        if self.request.method != "GET":
            return CreateAreaSerializer
        return AreaSerializer         

import json
from django.db import IntegrityError
@api_view(['POST'])
def import_data_from_json(request):
    try:
        # file_path = '\\shopdiy_b2c\\shop-diy-db\\pincode.json'
        file_path = '/home/ubuntu/shop-diy-db/pincode.json'
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        india, created = Country.objects.get_or_create(country_name='India',   )

        if isinstance(json_data, dict):
            states_to_create = []
            cities_to_create = []
            areas_to_create = []
            errors = []

            for state_name, cities in json_data.items():
                state, created = State.objects.get_or_create(country=india, state_name=state_name,   )
                states_to_create.append(state)

                for city_name, areas in cities.items():
                    city, created = CityOrTown.objects.get_or_create(state=state, city_name=city_name.strip(),   )
                    cities_to_create.append(city)

                    for area_name, pincode in areas.items():
                        area = Area(city=city, name=area_name.strip(), pincode=pincode.strip(),   )
                        areas_to_create.append(area)

            try:
                State.objects.bulk_create(states_to_create)
            except IntegrityError as e:
                errors.append(str(e))

            try:
                CityOrTown.objects.bulk_create(cities_to_create)
            except IntegrityError as e:
                errors.append(str(e))

            try:
                Area.objects.bulk_create(areas_to_create)
            except IntegrityError as e:
                errors.append(str(e))

            if errors:
                return Response({'errors': errors}, status=400)
            else:
                return Response({'message': 'Data imported successfully'}, status=201)
        else:
            return Response({'error': 'JSON data is not in the correct format'}, status=400)
    except FileNotFoundError:
        return Response({'error': 'File not found'}, status=400)
    except json.JSONDecodeError as je:
        return Response({'error': f'JSON decoding error: {je}'}, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
