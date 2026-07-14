from django.urls import path
from . import views

urlpatterns=[
    path('add-to-cart',views.addProductToOrder,name='addToCart')
]
