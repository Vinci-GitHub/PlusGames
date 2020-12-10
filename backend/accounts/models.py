# モデルはmodels.Modelを継承する
from django.db import models
# インポート
from django.contrib.auth.models import AbstractUser


# テーブルを定義
class CustomUser(AbstractUser):
    """カスタムユーザーモデル"""

    verbose_name_plural = 'CustomUser'
    email = models.EmailField(verbose_name='メールアドレス', unique=True)
    username = models.CharField(verbose_name='ユーザ名', unique=True, max_length=18)

    def __str__(self):
        return self.username
