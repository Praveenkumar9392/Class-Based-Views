from django.db import models
from masters.models import BaseModel
from simple_history.models import HistoricalRecords
from user_data.models import User


class Role(BaseModel):
    role_name = models.CharField(help_text='role_name', max_length=100, unique=True)
    is_client_specific = models.BooleanField(default=False)
    user_specific = models.ForeignKey("user_data.user", on_delete=models.CASCADE, null=True, blank=True, related_name='user_roles')
    under_role = models.ForeignKey("accounts.role", on_delete=models.CASCADE, null=True, blank=True)
    
    history = HistoricalRecords(inherit=True)

    def __str__(self):
        return self.role_name
    
class UserAccount(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    staff_role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)
    history = HistoricalRecords(inherit=True)

