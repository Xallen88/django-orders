from django.contrib import admin
from .models import Product, Order, Shipping

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Shipping)
