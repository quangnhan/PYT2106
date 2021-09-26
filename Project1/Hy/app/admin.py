from django.contrib import admin
from .models import Product,Category,UserBuyProduct
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','imageUrl','price_start','date_post','date_end','category','user_post')
    search_fields = ['name']
    list_filter = ('category','name','date_post','date_end')
admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('id','name')
admin.site.register(Category, CategoryAdmin)

admin.site.register(UserBuyProduct)
