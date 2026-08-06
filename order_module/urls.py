from django.urls import path
from . import views

urlpatterns=[
    path('add-to-cart',views.addProductToOrder,name='addToCart'),
    path('user-basket',views.userBasketView,name='userBasket'),
    path('user-order-quantity',views.change_order_quantity,name='order_quantity_page')
]
