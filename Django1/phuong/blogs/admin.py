from django.contrib import admin
from .models import Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ['name', 'category', 'description']

admin.site.register(Blog) 
admin.site.register(Category) 