from rest_framework import serializers
from trade.models import TradePost


class TradePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePost
        fields = '__all__'
