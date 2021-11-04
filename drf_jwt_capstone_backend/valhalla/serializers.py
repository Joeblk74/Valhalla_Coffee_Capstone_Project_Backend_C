from typing import FrozenSet


from rest_framework import serializers
from .models import Coffee

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ['flavor', 'origin', 'description', 'price', 'user_id']