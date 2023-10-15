from django.contrib import admin
from .models import Description, Product, Category,Images

from django.contrib import admin

class DescriptionInline(admin.StackedInline):  # or admin.StackedInline
    model = Description
    extra =  1

class ImagesInline(admin.StackedInline):  # or admin.StackedInline
    model = Images
    extra =  1
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline,DescriptionInline]


# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
