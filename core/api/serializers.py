from rest_framework import serializers
from core.models import *


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'id',
            'name',
            'address',
            'categories',
            'websites',
        ]
