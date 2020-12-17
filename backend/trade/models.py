from django.db import models


class TradePost(models.Model):
    post_title = models.CharField(max_length=255)
    post_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trade_item = models.CharField(max_length=255)