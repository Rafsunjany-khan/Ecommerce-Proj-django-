from django.urls import path
from .import views


app_name = "cartOrderApp"

urlpatterns = [
    path('add-to-cart/', views.addToCart, name='addToCart'),
    path('cart-page/<str:cart_id>/', views.cart, name='cart'),
    path('cart-item-remove/<str:cartItem_id>/<str:cart_id>/', views.cartItem_remove, name='cartItem_remove'),
    path('create-order/<str:cart_id>/', views.createOrder, name='createOrder'),
    path('order-summary/<str:cart_id>/', views.orderSummary, name='orderSummary'),
    path('cancel-order/<str:order_id>/', views.cancelOrder, name='cancelOrder'),
    path('order-order/<str:order_id>/', views.orderCOD, name='orderCOD'),
    path('ssl-order/<str:order_id>/', views.orderSSL, name='orderSSL'),
    #path('<str:id>/', views.productDetail, name='productDetail'),


]