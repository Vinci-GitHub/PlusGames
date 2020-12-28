# モデルはmodels.Modelを継承する
from django.db import models
from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    name = models.CharField(max_length=200)


class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)


# テーブルを定義
class CustomUser(AbstractUser):
    """カスタムユーザーモデル"""
    email = models.EmailField(
        verbose_name='メールアドレス',
        max_length=200,
        unique=True
    )
    first_name = models.CharField(
        max_length=200,
    )
    last_name = models.CharField(
        max_length=200,
    )
    password = models.CharField(
        verbose_name='パスワード',
        max_length=200,
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True
    )
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
