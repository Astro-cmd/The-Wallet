from rest_framework import serializers
from . models import Budgets

class BudegetSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Budgets
        fields = '__all__'