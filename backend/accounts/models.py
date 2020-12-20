# モデルはmodels.Modelを継承する
from django.db import models


# インポート
from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    name = models.CharField(max_length=200)


class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)


# テーブルを定義
class CustomUser(AbstractUser):
    """カスタムユーザーモデル"""

    verbose_name_plural = 'CustomUser'
    email = models.EmailField(verbose_name='メールアドレス',max_length=200, unique=True)
    username = models.CharField(verbose_name='ユーザ名', unique=True, max_length=18)
    password = models.CharField(verbose_name='パスワード', max_length=200)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []