# モデルはmodels.Modelを継承する
from django.db import models


# インポート
from django.contrib.auth.models import AbstractUser


# テーブルを定義
class CustomUser(AbstractUser):
    """カスタムユーザーモデル"""

    verbose_name_plural = 'CustomUser'
    email = models.EmailField(verbose_name='メールアドレス',max_length=200, unique=True)
    username = models.CharField(verbose_name='ユーザ名', unique=True, max_length=18)
    password = models.CharField(verbose_name='パスワード', max_length=200)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []