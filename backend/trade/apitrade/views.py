from rest_framework import generics
from trade.models import TradePost
from trade.apitrade.serializers import TradePostSerializer


class ListView(generics.ListCreateAPIView):
    queryset = TradePost.objects.all().order_by('-id')
    serializer_class = TradePostSerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradePost.objects.all()
    serializer_class = TradePostSerializer
