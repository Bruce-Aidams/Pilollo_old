from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart 
from django.contrib.auth.models import User
from Product.models import Product
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.)
@staff_member_required
def admin_order_detail(request, order_id):
	order = get_object_404(Order, id=order_id)
	return render(request, 'shop/orders/detail.html', {'order': order })

def sales(product):
	s = Product.objects.get(id=product.id)
	s.sold += 1
	s.save()


				 

def order_create(request):
	cart = Cart(request)
	data = None
	if request.method == 'POST':

		form = OrderCreateForm(request.POST)
	
		if form.is_valid():

			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order,
										 product=item['product'],
										 price=item['price'],
										 quantity=item['quantity'])
				

				sales(item['product'])
			# clear the cart
			cart.clear()
			return render(request, 'shop/orders/created.html',{'order':order})
	else:
		form = OrderCreateForm()
	return render(request, 'shop/orders/create.html',{'cart':cart,'form':form,'id':data } )