from rest_framework import serializers
from .models import *

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["bill", 'dish', 'quantity', 'total']
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['dish'] = instance.dish
    #     return data
    

class BillSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = Bill
        fields = ['id', 'table', 'customer',"total_price","is_paid","is_active", 'orders']



