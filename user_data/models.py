from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomAccountManager
from masters.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.
Role_Status = (
    ("Admin","Admin"),
    ("StoreManager","StoreManager"),
    ("Customer","Customer")
)
class User(BaseModel,AbstractBaseUser, PermissionsMixin):
    full_name=models.CharField(max_length=200,null=True,blank=True)
    mobileno = models.CharField(max_length=12,unique=True)
    email = models.CharField(max_length=100,null=True,blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False,blank=True)
    last_login = models.DateTimeField(null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    role = models.CharField(max_length=200,choices=Role_Status,default="Customer")
    otp_generated_at = models.DateTimeField(blank=True, null=True)
    device_token = models.CharField(max_length=200,null=True,blank=True)
    objects = CustomAccountManager()
    
    history = HistoricalRecords(inherit=True)
    USERNAME_FIELD = 'email'
    
    class Meta:
        ordering = ("mobileno",)
        
    def __str__(self):
            return str(self.full_name)