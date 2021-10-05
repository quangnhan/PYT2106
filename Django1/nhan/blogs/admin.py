from django.contrib import admin
from .models import Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ['name', 'description', 'category']

admin.site.register(Blog, BlogAdmin) 
admin.site.register(Category) 