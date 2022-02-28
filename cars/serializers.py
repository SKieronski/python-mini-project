from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    car_url = serializers.ModelSerializer.serializer_url_field(
        view_name='car_detail'
    )

    class Meta:
        model = Car
        fields = ['id', 'car_url', 'photo_url', 'make', 'model', 'year', 'price']