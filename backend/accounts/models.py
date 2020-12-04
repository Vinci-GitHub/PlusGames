# モデルはmodels.Modelを継承する
from django.db import models
# インポート
from django.contrib.auth.models import AbstractUser


# テーブルを定義
class CustomUser(AbstractUser):
    """カスタムユーザーモデル"""

    class Meta:
        # テーブル名を定義
        verbose_name_plural = 'CustomUser'
