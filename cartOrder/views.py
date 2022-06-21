from django.shortcuts import render, redirect, HttpResponse
from .models import *
from homepage.models import Products
from django.urls.base import reverse

def addToCart(request):
    print('-'*50)
    print('Add to Cart function is called!')

    if request.method == "POST":
         print('Product ID: ', request.POST['prod_id'] )
         print('Quantity: ', request.POST['prod_quant'] )
         print('Cart ID: ', request.POST['cart_id'] )

         prod_id = request.POST['prod_id']
         prod_quant = int(request.POST['prod_quant'])
         cart_id = request.POST['cart_id']

         prod = Products.objects.get(pk=prod_id)

         cart = Cart.objects.get(cart_id=cart_id)

         print('Product Instance (after query): ', prod)
         print('Product ID (after query): ', prod.id)
         print('Cart Instance (after query): ', cart)
         print('Cart ID (after query): ', cart.cart_id)
         print('Product Quantity: ', prod_quant)
         print('Product Price: ', prod.price)

         single_unit_price = prod.price

         total_prod_price = prod_quant * single_unit_price

         print('Total Price of Product (regarding quantity): ', total_prod_price)

         # Insert Product Into CartItem
         CartItem.objects.create(cart_id=cart, prod_id=prod, prod_quantity=prod_quant, prod_price=total_prod_price)
         print('Create a new cart-item is created for the customer-cart:  \'%s\'' % cart_id)

    print('-'*50)

   # return redirect('homepageApplication:homepage')
    return redirect(reverse(
        'cartOrderApp:cart',
        kwargs={'cart_id': cart_id}
     ))
    #return redirect('cartOrderApplication:cart')


# Create your views here.
def cart(request, cart_id):
    print('-' * 50)
    print('Cart function is called!')
    print('-' * 50)

    cart = Cart.objects.get(cart_id=cart_id)
    cartItems = CartItem.objects.filter(cart_id=cart)

    #for cit in cartItems:
        #print(cit.prod_id.name)

   # if request.method == "POST":
        # print('Product ID: ', request.POST['prod_id'])
        # print('Quantity: ', request.POST['prod_quant'])

   # prod = Products.objects.all()
   # for p in prod:
    #    print('product:', p)

    context={
        'title': 'Shopping Cart',
        'cart' : cart,
        'cart_id': cart_id,
        'cartItems': cartItems,
    }
    return render( request, 'cartOrder/cart.html', context)


def cartItem_remove(request, cartItem_id, cart_id):

    #print("Cart item removed!!!")
    #print("Cart Item ID:", cartItem_id)
    #print("Cart ID:", cart_id)

    if request.method == "POST":
        print('#' * 50)
        print('Cart Item ID(Post Method): ', cartItem_id)
        print('#' * 50)
        cart_Item = CartItem.objects.get(cartItem_id=cartItem_id)
        print('cart Item Instance: ', cart_Item)
        cart_Item.delete()

        #return HttpResponse("Cart Item function is called!! ")
        #return redirect()

    return redirect(reverse(
        'cartOrderApplication:cart',
        kwargs={'cart_id': cart_id}
    ))

def createOrder(request, cart_id):
    print('Create order function is called!')
    cust = User.objects.get(username=request.user)
    cart = Cart.objects.get(cart_id=cart_id)
    price = cart.total_price

    print('Create order function -----cart:', cart)

    order = Order.objects.filter(cart_id=cart, is_paid=False, is_cancelled=False)

    print("#" * 50)
    for o in order:
        print("Create (Order Function): ", o)
    print("#" * 50)

    if len(order) == 0:
        print("Create a new Order (createOrder function)!")
        Order.objects.create(
            customer=cust,
            cart_id=cart,
            price=price,
    )
    else:
        print("The order will be update (createOrder function)!")
        for o in order:
            o.price = price
            o.save()

    return redirect(reverse(
        'cartOrderApp:orderSummary',
        kwargs={ 'cart_id': cart_id }
    ))
    #return HttpResponse('A new order is generated!')




def orderSummary(request, cart_id):
    print('Order summery function is called')

    cart = Cart.objects.get(cart_id=cart_id)
    cartItems = CartItem.objects.filter(cart_id=cart)

    context = {
        'title': 'Order Summary',
        'cart': cart,
        'cart_id': cart_id,
        'cartItems': cartItems,
    }
    return render(request, 'cartOrder/order.html', context)
    #return HttpResponse('Order summery page is rendered')
    pass