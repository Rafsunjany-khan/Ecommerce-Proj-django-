from django.urls import path
from .import views


app_name = "cartOrderApp"

urlpatterns = [
    path('add-to-cart/', views.addToCart, name='addToCart'),
    path('cart-page/<str:cart_id>/', views.cart, name='cart'),
    path('cart-item-remove/<str:cartItem_id>/<str:cart_id>/', views.cartItem_remove, name='cartItem_remove'),
    #path('<str:id>/', views.productDetail, name='productDetail'),


]