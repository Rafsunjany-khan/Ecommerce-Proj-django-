from django.urls import path
from .import views

app_name = "homepageApp"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<str:id>/', views.productDetail, name='productDetail'),


]