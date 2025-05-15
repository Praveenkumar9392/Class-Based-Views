from blogapp.models import Blog,Blogcategory,Bookings,Contacts
from rest_framework import serializers

class BlogcategorySerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Blogcategory
        fields = ['id','title','is_active','image','sort','slug','is_suspended']
        depth = 1
    
    def get_slug(self,obj):
        return obj.get_slug()  
         
class CreateBlogcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogcategory
        fields = ['id','title','is_active','image','sort','is_suspended']
 
class BlogSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    category_slug = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['id','category','keywords','meta_description','title','content','image','is_active','sort','slug','is_suspended','category_slug']
        depth=1
    def get_slug(self,obj):
        return obj.get_slug()
    def get_category_slug(self,obj):
        return obj.category.get_slug()

class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','category','keywords','meta_description','title','content','image','is_active','sort','is_suspended'] 

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'    

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'  

    def validate(self, data):
        errors = []

        if data.get("main_frame", 0) < 5:
            errors.append("Main frame cannot be less than 5.")

        if data.get("ramp_pair", 0) < 2:
            errors.append("Ramp pair cannot be less than 2.")

        if errors:
            raise serializers.ValidationError({"error": errors})

        return data 