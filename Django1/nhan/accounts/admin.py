from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomerUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}), 
    )
    add_fieldsets = (
        (None, {'fields': ('phone',)}), 
        (None, {'fields': ('email',)})
    ) + UserAdmin.add_fieldsets 


admin.site.register(CustomUser, CustomerUserAdmin)