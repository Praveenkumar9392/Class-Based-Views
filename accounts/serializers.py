from .models import User,UserAccount
from rest_framework import serializers

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','role','is_suspended']

class CreateUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'user','staff_role', 'is_suspended']

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'user','staff_role', 'is_suspended']
        depth =1

