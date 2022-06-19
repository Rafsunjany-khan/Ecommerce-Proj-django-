from django.urls import path
from . import views

app_name = 'authApp'

urlpatterns = [
    path('reg/', views.userReg, name='userReg'),
]