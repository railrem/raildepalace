from rest_framework import serializers
from beer.models import Beer
class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = '__all__'