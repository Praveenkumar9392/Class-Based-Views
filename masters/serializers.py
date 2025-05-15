from masters.models import *
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name','is_suspended'] 

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name','country','is_suspended']
        depth = 2

class CreateStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name','country','is_suspended']

class CityOrTownSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityOrTown
        fields = ['id', 'city_name','state','is_suspended']
        depth = 2

class CreateCityOrTownSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityOrTown
        fields = ['id', 'city_name','state','is_suspended']         

class AreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Area
        fields = ['id', 'pincode', 'name','city','is_suspended']
        depth = 2


class CreateAreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Area
        fields = ['id', 'pincode', 'name','city','is_suspended']                                     