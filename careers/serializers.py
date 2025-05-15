from rest_framework import serializers
from .models import JobCategory, JobListing, JobApplication


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id','category','is_suspended']
        depth =1

class CreateJobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id','category','is_suspended']


class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['id','job_id', 'title', 'description', 'category', 'location', 'no_of_positions', 'applications', 'posted_date', 'deadline','is_suspended']
        depth = 1

class CreateJobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['id','job_id', 'title', 'description', 'category', 'location', 'no_of_positions', 'applications', 'posted_date', 'deadline','is_suspended']


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'job', 'full_name', 'email', 'phone_number', 'resume', 'cover_letter', 'applied_date', 'status','is_suspended']
        depth = 1

class CreateJobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'job', 'full_name', 'email', 'phone_number', 'resume', 'cover_letter', 'applied_date', 'status','is_suspended']
