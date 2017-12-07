from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Max
from . import models

class UserError (Exception):
	def __init__(self, value):
		self.value=value
	def __str__(self):
		return repr(self.value)

@login_required
def index_view (request):
	return redirect ('account')

@login_required
def account_view (request):
	shipping_info = models.Shipping.objects.get(user_id=request.user.id)
	return render(request, 'account.html', {'shipping_info': shipping_info})

@login_required
def shop_view (request):
	product_list = models.Product.objects.filter()
	category_list = []
	for p in product_list:
		if p.product_category not in category_list:
			category_list.append(p.product_category)
	return render(request, 'shop.html', {'product_list': product_list, 'category_list': category_list})

@login_required
def history_view (request):
	order_history = models.Order.objects.select_related('product_id').filter(user_id=request.user.id)
	return render(request, 'history.html', {'order_history': order_history})

def submit_view (request):
	try:
		product_length = models.Product.objects.count()
		post_keys = [str(p) + 'q' for p in range(1, product_length+1)]
		if max([int(request.POST[pkey]) for pkey in post_keys]) == 0:
			raise UserError("You did not add items to your order.")
	except (UserError):
		return shop_view(request)
	else:
		order_number = models.Order.objects.all().aggregate(Max('order_id'))['order_id__max'] + 1
		for p in range(1, product_length+1):
			k = str(p) + 'q'
			q = int(request.POST[k])
			if q != 0:
				product_entry = models.Product.objects.get(pk=p)
				order_entry = models.Order(order_id=order_number, user_id=request.user, product_id=product_entry, 
					order_description=request.user.first_name+' / '+product_entry.product_description,	
					order_quantity=q, order_date=timezone.now(), order_approved=None)
				order_entry.save()
		return HttpResponseRedirect(reverse('history'))
