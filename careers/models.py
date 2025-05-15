from django.db import models
from django.utils import timezone
from masters.models import BaseModel
from simple_history.models import HistoricalRecords


# Create your models here.

class JobCategory(BaseModel):
    category = models.CharField(max_length=200)  
    
    is_suspended = models.BooleanField(default=False)

    history = HistoricalRecords(inherit=True)
    
    def __str__(self):
        return self.category


class JobListing(BaseModel):
    job_id = models.CharField(max_length=200) 
    title = models.CharField(max_length=200)  
    description = models.TextField()  
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE) 
    location = models.CharField(max_length=200)  
    no_of_positions = models.IntegerField()  
    applications = models.IntegerField(default=0)  
    posted_date = models.DateTimeField(auto_now_add=True) 
    deadline = models.DateTimeField()
    
    is_suspended = models.BooleanField(default=False)

    history = HistoricalRecords(inherit=True)
    def __str__(self):
        return self.title


class JobApplication(BaseModel):
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)  
    full_name = models.CharField(max_length=100) 
    email = models.EmailField()  
    phone_number = models.CharField(max_length=20) 
    resume = models.FileField(upload_to='resumes/')  
    cover_letter = models.TextField()  
    applied_date = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=50, default='Pending')  
    
    is_suspended = models.BooleanField(default=False)

    history = HistoricalRecords(inherit=True)
    def __str__(self):
        return f"{self.full_name} - {self.job.title}"

    def update_status(self, new_status):
        self.status = new_status
        self.save()