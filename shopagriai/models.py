from msilib.schema import Property
from unicodedata import name
from django.db import models
import datetime
from django.contrib.auth.models import User
import uuid

#categories of products
class Category(models.Model):
    name=models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/category/', blank=True, null=True)
    
    
    
    def __str__(self):
        return self.name
    
    class Meta:
		    verbose_name_plural = 'categories'
  
  
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='uploads/products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#Order Model
class Order(models.Model):
        ORDER_STATUS_CHOICES = [
            ('Pending', 'Pending'),
            ('Processing', 'Processing'),
            ('Shipped', 'Shipped'),
            ('Delivered', 'Delivered'),
        ]
        customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
        date_ordered = models.DateTimeField(auto_now_add=True)
        complete = models.BooleanField(default=False)
        transaction_id = models.CharField(max_length=100, null=True)
        status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')


        def __str__(self):
            return str(self.id)
        @property
        def shipping(self):
            shipping=False
            orderitems=self.orderitem_set.all()
            for i in  orderitems:
                shipping=True
            return shipping
        
        @property
        def get_cart_total(self):
            order_items = self.orderitem_set.all() 
            total = sum([item.get_total for item in order_items]) 
            return total
        @property
        def get_cart_items(self):
            orderitems = self.orderitem_set.all()
            total = sum([item.quantity for item in orderitems])
            return total

#Orderitem <--Because cart can have multiple order-->
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)
    @property
    def get_total(self):
        total = self.product.price * self.quantity 
        return total
        
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
        
 

 
 
#Shipping address:
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)

	def __str__(self):
		return self.address

