from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe



STATUS_CHOICES = (
    ('PROCESS', 'Processing'),
    ('SHIPPED', 'Shipped'),
    ('DELIVERED', 'Delivered'),
)

STATUS = (
    ("DRAFT", 'Draft'),
    ("DISABLED", 'Disable'),
    ("REVIEW", 'Review'),
    ("PUBLISHED", 'Publish'),
)

RATING_CHOICES = (
    (1, '⭐☆'),
    (2, '⭐⭐☆☆'),
    (3, '⭐⭐⭐☆☆☆'),
    (4, '⭐⭐⭐⭐☆☆☆☆'),
    (5, '⭐⭐⭐⭐⭐☆☆☆☆☆'),
)


class Category(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Vendor(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='vendor_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True, default="This is the product")
    address = models.CharField(max_length=255, default="Monrovia")
    contact = models.CharField(max_length=20, default="(+231779005985)")  # Assuming contact is a phone number
    cart_resp_time = models.IntegerField()  # Response time for cart, in minutes
    shipping_on_time = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Vendor's user
    authentic_rating = models.DecimalField(max_digits=3, decimal_places=2, default="100")  # Authentic rating out of 10
    day_return = models.CharField(max_length=100, default="100")  # Days allowed for return
    wyt_period = models.CharField(max_length=100, default="100")  # Warranty period in months

    def vendor_image(self):
        return mark_safe('<img src="%s", width="50", height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default="0.00", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    min_price = models.DecimalField(max_digits=5, decimal_places=2, default="0")
    max_price = models.DecimalField(max_digits=5, decimal_places=2, default="0")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default="0.00", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Vendor's user
    specification = models.TextField(null=True, blank=True)
    produc_status = models.CharField(max_length=20, choices=STATUS, default="processing")
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True, default=0) 
    featured = models.BooleanField(default=False) 
    date = models.DateField(auto_now_add=True)  


    def product_image(self):
        return mark_safe('<img src="%s", width="50", height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/', null=True, default=0)
    image3 = models.ImageField(upload_to='product_images/', null=True, default=0)
    thumbnail = models.ImageField(upload_to='product_thumbnails/')

      
    def __str__(self):
        return str(self.image.url)
    
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    
    def __str__(self):
        return self.user

class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    image = models.ImageField()
    qty = models.IntegerField(default=0)
    product_status = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=5, decimal_places=2, default="1.99")
    
    
    def __str__(self):
        return self.item

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True) 

    
    def __str__(self):
        return self.user
    
class BlogPost(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    pub_date = models.DateField()
    comment_count = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content_url = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    create_account = models.BooleanField(default=False)
    account_password = models.CharField(max_length=50, null=True, blank=True)
    ship_different = models.BooleanField(default=False)
    order_notes = models.TextField(null=True, blank=True)
    payment_method = models.CharField(max_length=20)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} - {self.first_name} {self.last_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"OrderItem {self.id}"