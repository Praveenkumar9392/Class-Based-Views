from django.db import models
from catlog.models import SeoUrl
from masters.models import BaseModel
from simple_history.models import HistoricalRecords
from mediamanager.models import MediaItem

class Blogcategory(BaseModel):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    image = models.ForeignKey(MediaItem,on_delete=models.SET_NULL,null=True)
    sort = models.IntegerField()   
    

    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return u'%s' % self.title  
    
    def get_slug(self):
        try:
            return SeoUrl.objects.get(content_type__model="blogcategory",object_id=self.id).keyword
        except:
            return ""
    
class Blog(BaseModel):
    category = models.ForeignKey(Blogcategory, on_delete=models.CASCADE)
    keywords = models.TextField(null=True,blank=True)
    meta_description = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField() 
    image = models.ForeignKey(MediaItem,on_delete=models.SET_NULL,null=True)
    is_active = models.BooleanField(default=True)
    sort = models.IntegerField()   
    

    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return u'%s' % self.title  
    
    def get_slug(self):
        try:
            return SeoUrl.objects.get(content_type__model="blog",object_id=self.id).keyword
        except:
            return ""

           
STATUS = (("New","New"), 
        ("Followup","Followup"), 
        ("Cancelled","Cancelled"),
        ("Converted","Converted"),
        ("Closed","Closed"))
class Contacts(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=20)
    message = models.TextField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=200,choices=STATUS,default="New")
    history = HistoricalRecords(inherit=True)
    
    def __str__(self):
        return u'%s' % self.name  
    
class Bookings(BaseModel):
    product_name = models.CharField(max_length=500)
    full_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    location = models.CharField(max_length=200)
    from_date = models.DateField()
    to_date = models.DateField()
    message = models.TextField()
    main_frame = models.IntegerField(null=True,blank=True)
    ramp_pair = models.IntegerField(null=True,blank=True)
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return u'%s' % self.full_name