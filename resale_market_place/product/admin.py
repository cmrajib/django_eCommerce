
from django.contrib import admin
from product.models import Product, Category, Brand


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}



admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
