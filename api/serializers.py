from rest_framework import serializers
from .models import Order, status

class orderSerializer(serializers.ModelSerializer):
    productName = serializers.CharField(source='productId.productName', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'productId', 'productName', 'amount', 'customerId', 'status', 'transactionDate', 'createdBy', 'createdOn']

class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = status
        fields = ['id', 'name']