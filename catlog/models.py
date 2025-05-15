from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from masters.models import BaseModel
from simple_history.models import HistoricalRecords
from mediamanager.models import MediaItem
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class SeoUrl(BaseModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    keyword = models.SlugField(max_length=200)
    

    history = HistoricalRecords(inherit=True)

    class Meta:
        unique_together = ('keyword','object_id','content_type')

    def __str__(self):
        return "{}".format(self.keyword)   

class InformationPage(BaseModel):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
        ('Archived', 'Archived'),
    )

    pagename = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    is_priority = models.BooleanField(default=False)
    sort = models.PositiveIntegerField()
    meta_title = models.CharField(max_length=200,null=True,blank=True)
    meta_description = models.TextField(null=True,blank=True)
    meta_keyword = models.TextField(null=True,blank=True)
    
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return self.pagename  

    def get_slug(self):
        try:
            return SeoUrl.objects.get(content_type__model="informationpage",object_id=self.id,).keyword
        except:
            return ""  
        

class Policy(BaseModel):
    faq = models.TextField(null=True,blank=True)
    return_policy = models.TextField(null=True,blank=True)
    cancellation = models.TextField(null=True,blank=True)
    privacy_policy = models.TextField(null=True,blank=True)
    about_us = models.TextField(null=True,blank=True)
    terms_conditions = models.TextField(null=True,blank=True) 
    is_suspended = models.BooleanField(default=False) 
    

    history = HistoricalRecords(inherit=True)
    def __str__(self):
        return self.privacy_policy 

class AdditionalSitemapUrl(BaseModel):
    slug = models.SlugField(unique=True, max_length=255)
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return self.slug
    
class RedirectRouter(BaseModel):
    old_slug = models.SlugField(unique=True)
    seourl = models.ForeignKey(SeoUrl,on_delete=models.CASCADE)

    history = HistoricalRecords(inherit=True)   

    def __str__(self) -> str:
        return self.old_slug
    

@receiver(post_save, sender=SeoUrl)
def slug_update(sender, instance, **kwargs):
    RedirectRouter.objects.filter(old_slug=instance.keyword, seourl=instance).delete()
    history_records = instance.history.order_by('-mdate')
    if history_records.count() > 1:
        last_history = history_records[1]
        old_slug = last_history.keyword
        if old_slug != instance.keyword:
            RedirectRouter.objects.create(
                old_slug=old_slug,
                seourl=instance
            )

class Scrolling_News(BaseModel):
    scrolling_point = models.CharField(max_length=200)
    scrolling_upto = models.DateField()
    history = HistoricalRecords(inherit=True)

    def _str_(self):
        return self.scrolling_point