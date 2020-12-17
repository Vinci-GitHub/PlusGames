from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .serializers import AccountsSerializer

# データを設定できるようにレジスタ関数を作成する


@api_view(['POST'])
def register(request):
    data = request.data

    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Passwords do not match!')

    serializer = AccountsSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)




@api_view(['GET'])
def accounts(request):
    serializer = AccountsSerializer(CustomUser.objects.all(), many=True)
    return Response(serializer.data)
