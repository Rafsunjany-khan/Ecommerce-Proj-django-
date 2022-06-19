from django.urls import path
from .import views


app_name = "cartOrderApp"

urlpatterns = [
    path('add-to-cart/', views.addToCart, name='addToCart'),
    path('cart-page/<str:cart_id>/', views.cart, name='cart'),
    path('cart-item-remove/<str:cartItem_id>/<str:cart_id>/', views.cartItem_remove, name='cartItem_remove'),
    path('create-order/<str:cart_id>/', views.createOrder, name='createOrder'),
    #path('create-summary/', views.orderSummary, name='orderSummary'),
    #path('<str:id>/', views.productDetail, name='productDetail'),


]