from django.contrib import admin
from account.models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomerUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}), 
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone',)}), 
        (None, {'fields': ('email',)})
    ) 


admin.site.register(CustomUser, CustomerUserAdmin)
