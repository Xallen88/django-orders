from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product (models.Model):
	product_name = models.CharField(max_length=100)
	product_description = models.CharField(max_length=400)
	product_category = models.CharField(max_length=100)
	product_price = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__ (self):
		return self.product_name + ' (' + str(self.pk) + ')'

class Order (models.Model):
	order_id = models.IntegerField()
	user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order_description = models.CharField(max_length=100)  #Record the product name in case it gets deleted
	order_quantity = models.IntegerField(default=1)
	order_date = models.DateField()
	order_approved = models.NullBooleanField()

	def __str__ (self):
		return self.order_description + ' (' + str(self.order_id) + ')'

class Shipping (models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	shipping_address = models.CharField(max_length=100)
	shipping_postalcode = models.CharField(max_length=8)
	shipping_city = models.CharField(max_length=100)
	shipping_province = models.CharField(max_length=100)

	def __str__ (self):
		return self.shipping_address
