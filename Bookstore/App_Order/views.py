from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, Order
from App_Shop.models import product
from django.contrib.auth.decorators import login_required
@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(product, pk=pk)
    order_item, created = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        # Check if the item is already in the cart
        if order.order_items.filter(item=item).exists():
            order_item = Cart.objects.get(item=item, user=request.user, purchased=False)
            order_item.quantity += 1
            order_item.save()
        else:
            order.order_items.add(order_item)

    else:
        order = Order(user=request.user)
        order.save()
        order.order_items.add(order_item)

    return redirect("App_Shop:home")

@login_required
def cart_view(request):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    
    if order_qs.exists():
        order = order_qs[0]
        order_items = order.order_items.all()

        context = {
            'order_items': order_items,
        }

        return render(request, 'App_Order/cart.html', context)
    else:
        # No active cart, handle this case as needed
        return redirect("App_Shop:home")




        