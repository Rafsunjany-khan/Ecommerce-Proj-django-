from django.db import models
#from homepage.models import Products
from homepage.models import *
import string, random
from django.contrib.auth.models import User



def random_string_generator(size=20, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length= 100, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer+', verbose_name='customer')
    is_ordered = models.BooleanField(default=False)
    total_cart_items = models.PositiveBigIntegerField(default=0)
    total_price = models.FloatField(default=0)

    class Meta():
        verbose_name_plural = 'shopping cart'


    def __str__(self)-> str:
        return self.cart_id

    def save(self, *args, **kwargs):
         if len(self.cart_id) == 0:
              self.cart_id = str(self.customer) + "_" + random_string_generator()
         super(Cart, self).save(*args, **kwargs)


class CartItem(models.Model):
    cartItem_id = models.CharField(max_length= 100, blank=True)
    cart_id = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    prod_quantity = models.IntegerField()
    prod_price = models.FloatField(default=0)


    class Meta():
        verbose_name_plural = 'shopping Cart Items'

    def __str__(self) -> str:
        return self.cartItem_id

    def save(self, *args, **kwargs):
        if not len(self.cartItem_id):
            self.cartItem_id = str(self.cart_id) + '_' + random_string_generator()

        # Print('prod price: ', self.prod_id.price * self.prod_quantity)
        self.prod_price = self.prod_id.price * self.prod_quantity
        super(CartItem, self). save(*args, **kwargs)


PAYMENT_CHOICES = [
    ('COD', 'COD'),
    ("SSLCommerz", 'SSLCommerz'),
]

class Order(models.Model):
    order_id = models.CharField(verbose_name='Order ID', max_length=100)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer+', verbose_name='Customer')
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    payment_method = models.CharField(verbose_name='Payment Method', max_length=20, choices=PAYMENT_CHOICES, default='COD')
    is_paid = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    delivery_address = models.TextField(verbose_name='Delivery Address', blank=True)
    delivery_time = models.DateField(verbose_name='Delivery Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Order"

    def __str__(self) -> str:
        return self.order_id

    def save(self, *args, **kwargs):
        #if no 'order_id' isnt passed while creating an order.

        if not len(self.order_id):
            self.order_id = 'order_' + str(self.customer) + "_" + random_string_generator()

        super(Order, self).save(*args, **kwargs)
