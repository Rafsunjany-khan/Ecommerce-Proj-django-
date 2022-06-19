from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete
from .models import *


@receiver(pre_save, sender=CartItem)
def update_price2(sender, **kwargs):
    cart_items = kwargs['instance']
    print('CartItem Prod Quantity (from signals: )', cart_items.prod_quantity)
    print('CartItem Price (from signals: )', cart_items.prod_price)

    total_cart_items = CartItem.objects.filter(cart_id=cart_items.cart_id).all()

    cart = Cart.objects.get(cart_id=cart_items.cart_id)
    print('Cart (from signals:)', cart)

    totalQuantity = cart_items.prod_quantity

    print('Total Cart Item Product Quantity: ', totalQuantity)

    cart.total_cart_items += totalQuantity
    cart.total_price += cart_items.prod_price
    cart.save()


@receiver(pre_delete, sender=CartItem)
def update_price(sender, **kwargs):
    cart_items = kwargs['instance']
    print('CartItem Prod Quantity (from signals: )', cart_items.prod_quantity)
    print('CartItem Price (from signals: )', cart_items.prod_price)

    total_cart_items = CartItem.objects.filter(cart_id=cart_items.cart_id).all()

    cart = Cart.objects.get(cart_id=cart_items.cart_id)
    print('Cart (from signals:)', cart)

    totalQuantity = cart_items.prod_quantity

    print('Total Cart Item Product Quantity: ', totalQuantity)

    cart.total_cart_items -= totalQuantity
    cart.total_price -= cart_items.prod_price
    cart.save()


