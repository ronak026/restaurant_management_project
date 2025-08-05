from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    STATUS_CHOICES  = [
        ('PENDING', 'pending'),
        ('PROCESSING', 'processing'),
        ('COMPLETED', 'completed'),
        ('CANCELED', 'canceled'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"