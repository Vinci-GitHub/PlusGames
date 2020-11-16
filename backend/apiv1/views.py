from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop.models import Game
from .serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    """ゲームモデルのCRUD用のAPIクラス"""

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
