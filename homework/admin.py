from django.contrib import admin
from homework.models import Product, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'preview', 'price', 'category')
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
