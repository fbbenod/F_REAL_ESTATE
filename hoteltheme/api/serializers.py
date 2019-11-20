from rest_framework import serializers
from listings.models import Listing
from realtors.models import Realtor


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('realtor', 'title', 'address', 'city', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size',
                  'photo_main')


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = ('name', 'photo', 'description', 'phone', 'email', 'is_mvp', 'hire_date')
