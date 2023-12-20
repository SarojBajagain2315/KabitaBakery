from django.urls import path
from .views import *


urlpatterns=[
    path('',homepage),
    path('productdetails/<int:product_id>',productdetails),
    path('products/',showproducts),
    path('addtocart/<int:product_id>',add_to_cart),
    path('showcart/',show_cart_items),
    path('deletecartitem/<int:cart_id>',delete_cart_items),
    path('order/<int:product_id>/<int:cart_id>',order_item),
    path('myorder/',my_order),
    path('esewa_verify/',esewa_verify),
    

]