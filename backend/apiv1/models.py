import uuid
from django.db import models
from django.utils import timezone


class Game(models.Model):
    """ゲームモデル"""
    class Meta:
        db_table = 'game'
        ordering = ['created_at']
        verbose_name = verbose_name_plural = 'ゲーム'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=20, unique=True)

    price = models.IntegerField(verbose_name='価格', null=True)

    def __str__(self):
        return self.title
