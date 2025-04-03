from django.db import models

# Create your models here.
# models.py
from django.db import models
import uuid

class SoilTestRequest(models.Model):
    STATUS_CHOICES = [
        ('Request Accepted', 'Request Accepted'),
        ('Denied', 'Denied'),
        ('Sample Collected', 'Sample Collected'),
        ('Arrived at Lab', 'Arrived at Lab'),
        ('Pending','Pending'),
        ('Test Completed', 'Test Completed'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    nitrogen = models.FloatField(null=True, blank=True)
    phosphorus = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)
    pH = models.FloatField(null=True, blank=True)
    copper = models.FloatField(null=True, blank=True)
    boron = models.FloatField(null=True, blank=True)
    sulfur = models.FloatField(null=True, blank=True)
    iron = models.FloatField(null=True, blank=True)
    zinc = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.full_name
