from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="product_list"),
    path('customer', customer, name="customer_list"),
    path('seller', seller, name="seller_list"),
    path('order', order, name="order_list"),
    path('report', report, name='report'),
    path('report2', report2, name='report2'),
    path('report3', report3, name='report3'),
    path('report4', report4, name='report4'),
    path('update_item/<int:product_id>', update_item, name="update_item"),
    path('update_item_customer/<int:customer_id>', update_item_customer, name="update_item_customer"),
    path('update_item_seller/<int:seller_id>', update_item_seller, name="update_item_seller"),
    path('update_item_order/<int:order_id>', update_item_order, name="update_item_order"),

]
