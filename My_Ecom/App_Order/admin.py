from django.contrib import admin

# Register your models here.
from App_Order.models import Cart, Order

admin.site.register(Cart)
admin.site.register(Order)