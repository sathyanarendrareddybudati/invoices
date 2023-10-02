from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ['customer_name']
