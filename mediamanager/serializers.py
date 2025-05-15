from .models import MediaFolder,MediaItem
from rest_framework import serializers

class MediaFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFolder
        fields = ['id','name','parent_folder','is_suspended'] 
       
        
class MediaItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, read_only=True)
    class Meta:
        model = MediaItem
        fields = ['id','name','folder','image','is_suspended','is_trash'] 
        depth=1
       
class CreateMediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItem
        fields = ['id', 'name', 'is_suspended','folder','image']       
