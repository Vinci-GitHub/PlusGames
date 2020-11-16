from rest_framework import serializers

from shop.models import Game


class GameSerializer(serializers.ModelSerializer):
    """ゲームモデル用のシリアライザ"""

    class Meta:
        # 対象のモデルクラスを指定
        model = Game
        # 利用するモデルのフィールドを指定
        fields = ['id', 'title', 'price']
