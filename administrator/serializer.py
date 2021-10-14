from django.contrib.auth import models
from rest_framework import fields, serializers

from core.models import Link, Product, OrderItem, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField('get_total')

    def get_total(self, obj):
        items = OrderItem.objects.filter(order_id=obj.id)
        return (sum((o.price * o.quantity) for o in items))

    class Meta:
        models = Order
        fields = '__all__'
