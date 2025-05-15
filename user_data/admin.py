from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('mobileno', 'full_name','is_staff', 'is_superuser')
    readonly_fields = ('last_login', 'date_joined',)
    ordering = ('mobileno',)
    search_fields = ('mobileno', 'email','full_name',)  
    fieldsets = (
        (
            'Fields',
            {
                'fields': (
                    'email',
                    'full_name',
                    'mobileno',
                    'date_joined',
                    'last_login',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'otp',
                    'user_permissions',
                    'password',
                    'role',
                    'device_token'
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobileno','password1', 'password2'),
        }),
    )


admin.site.register(User, CustomUserAdmin)