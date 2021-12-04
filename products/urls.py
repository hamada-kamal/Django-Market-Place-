from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    
    path('',views.all_products , name='store'),
    path('autosearch',views.autoSearch , name='autosearch'),
    path('<slug:slug>', views.product_detail , name='detail'),
    path('<slug:slug>/likeItem', views.likeItem, name="like_item"),
    path('update_item/', views.updateItem, name="update_item"),
    path('cart/',views.cart , name='cart'),
    path('checkout/',views.checkout , name='checkout'),
    

    path('wish-list/', views.liked_product, name="liked_product"),
    path('process_order/', views.processOrder, name="process_order"),

] 