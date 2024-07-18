from django.contrib import admin
from . models import *
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'image', 'description', 'category', 'price', 'old_price', 'specification', 'produc_status', 'featured', 'date')


class productReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review', 'rating', 'date')



class vendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'image', 'description', 'address', 'contact', 'cart_resp_time', 'shipping_on_time', 'authentic_rating', 'day_return', 'wyt_period')



class cartOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'paid_status', 'order_date', 'product_status')


class cartOrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'image', 'qty', 'product_status', 'price', 'total')



class wishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'date')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('image', 'pub_date', 'comment_count', 'title', 'summary', 'content_url')

class ProductimageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'thumbnail')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country', 'address', 'address2', 'city', 'state', 'zipcode', 'phone', 'email', 'create_account', 'account_password', 'ship_different', 'order_notes', 'payment_method', 'subtotal', 'total', 'date_ordered')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'total') 

admin.site.register(Category)
admin.site.register(Product, productAdmin)
admin.site.register(Wishlist, wishListAdmin)
admin.site.register(ProductReview, productReviewAdmin)
admin.site.register(Vendor, vendorAdmin)
admin.site.register(CartOrder, cartOrderAdmin)
admin.site.register(CartOrderItem, cartOrderItemAdmin)
admin.site.register(BlogPost, BlogAdmin)
admin.site.register(ProductImage, ProductimageAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)