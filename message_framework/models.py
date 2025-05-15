from django.db import models
from accounts.models import User
from masters.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.


PRIORITY = (
    ("High","High"),
    ("Urgent","Urgent"),
    ("Medium","Medium"),
    ("Low","Low")
)

STATUS = (
    ("New","New"),
    ("Open","Open"),
    ("InProgress","InProgress"),
    ("Solved","Solved"),
    ("Closed","Closed")
)
class Ticket(BaseModel):
    title = models.CharField(max_length=200,null=True, blank=True)
    description = models.CharField(max_length=200,null=True, blank=True)
    service_type= models.CharField(max_length=255,null=True, blank=True)
    priority = models.CharField(max_length=50,choices=PRIORITY,null=True, blank=True)
    status = models.CharField(max_length=50,choices=STATUS,default="New")
    created_by = models.ForeignKey(User, related_name='created_tickets', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='assigned_tickets', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords(inherit=True)

class ChatRecord(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='chat_records', on_delete=models.CASCADE,null=True,blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(inherit=True)
    
class ChatOption(BaseModel):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_options')
    is_root = models.BooleanField(default=False)
    is_exit_option = models.BooleanField(default=False)

    history = HistoricalRecords(inherit=True)

class ChatOptionMessage(BaseModel):
    chat_option = models.ForeignKey(ChatOption, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField(null=True,blank=True)
    history = HistoricalRecords(inherit=True)

class welcomemessage(BaseModel):
    message = models.TextField()
    history = HistoricalRecords(inherit=True)

CALL_STATUS = (
    ("Inprogress","Inprogress"),
    ("Called","Called"),
    ("Solved","Solved"),
    ("Closed","Closed")
)
class ChatQueryLeads(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    mobileno = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    service = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255,choices=CALL_STATUS,default="Inprogress",null=True,blank=True)
    service_domain = models.CharField(max_length=255, null=True, blank=True)
    browser_type = models.CharField(max_length=255, null=True, blank=True)
    ipaddress = models.GenericIPAddressField(null=True, blank=True)
    history = HistoricalRecords(inherit=True)

class chatLogo(BaseModel):
    logo = models.ImageField(upload_to='chat_logo/')
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    history = HistoricalRecords(inherit=True)