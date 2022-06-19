from django.shortcuts import render, redirect, reverse
from .models import Products
from cartOrder.models import *
from django.contrib.auth.models import User


def homepage(request):

    # Get all products from "Product"  model from inside "ecommerceProj\homepage\models
    prods = Products.objects.all()

    print(User.objects.all())
    print('User:', request.user)
    print('User', request.user.id)

    # fetch the user instance
    cust = User.objects.get(id=request.user.id)
    print('Cust Instance:', cust)

    # check if there is any cart for the customer, if not, then create a new cart for customer
    custCart = Cart.objects.all()
    print(custCart)

    try:
        # Check for a cart of the customer,whose 'is_ordered' field is 'False'
        custCart = Cart.objects.filter(customer=cust, is_ordered=False).first()

        print("Customer Cart (Homepage):", custCart)
        print("Customer Cart ID:", custCart.cart_id)
    except:
        #print(custCart)
        #if no cart of that customer is found, then create a new cart for customer
        if not custCart:
            Cart.objects.create(customer=cust)
            print('Create a new cart of the customer: \'%s\'' % request.user)

            return redirect('homepageApp:homepage')

    context = {
        'title': 'Homepage',
        'Products': prods,
        'custCart': custCart,
        'cart_id': custCart.cart_id,
        }

    return render(request, 'homepage/index.html', context)


def productDetail(request, id):
    print('Product ID: ', id)

    # Query in the product db to fetch all the data about the product
    prod = Products.objects.get(pk=id)
    print('prod Name: ', prod.name)
    print('prod Price: ', prod.price)
    print('prod Description: ', prod.desc)

    print('Product Detail Information: ', prod)

    cust = User.objects.get(id=request.user.id)

    # check for a cart of that customer, whose 'is_ordered' field is 'False'.
    custCart = Cart.objects.filter(customer=cust, is_ordered=False).first()

    # print('Customer Cart:', custCart)
    cart_id = custCart.cart_id
    # print('Customer Cart ID:', custCart.cart_id)

    context = {
        'title': 'Product Detail',
        'productDetail': prod,
        'cart_id': cart_id,

    }
    return render(request, 'homepage/product_detail.html', context)
