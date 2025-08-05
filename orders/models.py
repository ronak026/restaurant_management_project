from django.db import models
from django.contrib.auth.models import User
from poducts.models import Item

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES  = [
        ('PENDING', 'pending'),
        ('PROCESSING', 'processing'),
        ('COMPLETED', 'completed'),
        ('CANCELED', 'canceled'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders') #Link to User
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items') #Link to Order Models
    menu = models.ForeignKey(Item, on_delete=models.CASCADE) #Link To Menu Model
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu.name}"