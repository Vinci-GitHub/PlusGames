from django.db import models
import accounts.models


class Thread(models.Model):
    owner = models.ForeignKey(accounts.models.CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    is_public = models.BooleanField(default=False)


