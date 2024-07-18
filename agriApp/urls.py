from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('category_view', views.category_view, name='category'),
    path('product_category/<int:category_id>/', views.product_category, name='product_category'),
    path('shopcart/', views.shopcart, name='shopcart'),

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),

    path('shop_detail/<int:id>/', views.shop_detail, name='shop_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/', views.shop_detail, name='blog_detail'),
    
    path('checkout/', views.checkout, name='checkout'),
    path('process_order/', views.process_order, name='process_order'),
    path('contact/', views.contact, name='contact'),
    
    path('delete_from_cart/', views.delete_from_cart, name='delete_from_cart'),
    
    path('product_search/', views.product_search, name='product_search'),
]

