from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from django.conf import settings
from django.core.exceptions import ValidationError
User = settings.AUTH_USER_MODEL

class BaseModel(models.Model):
    status_flag = models.BooleanField(default=True)
    comments = models.TextField(blank=True, null=True)
    active_from = models.DateTimeField(default=timezone.now)
    active_to = models.DateTimeField(null=True, blank=True)
    cdate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)
    cuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                              blank=True, related_name="%(app_label)s_%(class)s_base_cuser")
    muser = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                              blank=True, related_name="%(app_label)s_%(class)s_base_muser")
    is_deleted = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)

    class Meta:
        abstract = True
        
class Country(BaseModel):
    country_name = models.CharField(max_length=200)
    
    is_suspended = models.BooleanField(default=False)

    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return self.country_name


class State(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,null=True,blank=True)
    state_name = models.CharField(max_length=200)
    
    is_suspended = models.BooleanField(default=False)

    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return self.state_name


class CityOrTown(BaseModel):
    state = models.ForeignKey(State, on_delete=models.SET_NULL,null=True,blank=True)
    city_name = models.CharField(max_length=200)
    
    is_suspended = models.BooleanField(default=False)

    history = HistoricalRecords(inherit=True)
    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return u'%s' % self.city_name
    
class Area(BaseModel):
    pincode = models.CharField(max_length=6)
    name = models.CharField(max_length=200)
    city = models.ForeignKey(CityOrTown,on_delete=models.SET_NULL,null=True,blank=True)
    
    is_suspended = models.BooleanField(default=False)
    
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        # return f"{self.name} - {self.pincode}"
        return u'%s' % self.pincode
    