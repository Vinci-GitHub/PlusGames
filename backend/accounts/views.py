from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import generate_access_token, JWTAuthentication
from .models import CustomUser, Permission
from .serializers import AccountsSerializer, PermissionSerializer


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


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    accounts = CustomUser.objects.filter(email=email).first()

    if accounts is None:
        raise exceptions.AuthenticationFailed('User not found!')

    if not accounts.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect password')

    response = Response()

    token = generate_access_token(accounts)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response


@api_view(['POST'])
def logout(_):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        'message': 'Succes'
    }

    return response


class AuthenticatedUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = AccountsSerializer(request.accounts)

        return Response({
            'data': serializer.data
        })


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })
