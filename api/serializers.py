from rest_framework import serializers
from .models import Item, Address

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ItemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['description']  # descriptionフィールドのみを指定

