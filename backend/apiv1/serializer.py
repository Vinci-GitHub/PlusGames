from rest_framework import serializers
from . import models
import accounts as accounts_serializer


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Thread
        fields = '__all__'

