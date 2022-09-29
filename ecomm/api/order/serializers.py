from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= order
        fields = object.__all__
        #todo add product and quantity
