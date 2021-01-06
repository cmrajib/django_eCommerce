from django.contrib import admin

# Register your models here.
from App_Shop.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)