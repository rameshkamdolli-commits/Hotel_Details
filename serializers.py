from rest_framework import serializers
from .models import HotelDetails

class HotelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDetails
        fields = '__all__'