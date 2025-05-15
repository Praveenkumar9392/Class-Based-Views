from django.contrib import admin
from .models import JobApplication,JobListing,JobCategory
# Register your models here.
admin.site.register(JobApplication)
admin.site.register(JobListing)
admin.site.register(JobCategory)