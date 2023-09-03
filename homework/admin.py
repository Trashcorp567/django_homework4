from django.contrib import admin
from homework.models import Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'preview', 'description', 'price')
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)
