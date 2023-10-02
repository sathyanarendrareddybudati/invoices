from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    date = models.DateField(default=timezone.now)
    customer_name = models.CharField(max_length=255)

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
