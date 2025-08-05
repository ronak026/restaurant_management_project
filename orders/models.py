from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.model):
    STATUS_CHOICES  = [
        ('PENDING', 'panding'),
        ('PROCESSING', 'processing'),
        ('COMPLETED', 'completed'),
        ('CANCELLED', 'cancelled'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_items = models.ManyToManyField(Menu, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_palces=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"