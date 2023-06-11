from django.db import models
from django.utils import timezone


class Question(models.Model):
    body = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "質問"
        verbose_name_plural = "質問一覧"
