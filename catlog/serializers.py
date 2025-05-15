from rest_framework import serializers
from catlog.models import *

class SeoUrlSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = SeoUrl
        fields = ['id','content_type','object_id','keyword','is_suspended']
    
    def get_content_type(self,obj):
        return obj.content_type.model