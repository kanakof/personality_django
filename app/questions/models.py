from django.db import models
from django.utils import timezone

class Question(models.Model):
    body = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "質問"
        verbose_name_plural = "質問一覧"


class AnswerChoices(models.IntegerChoices):
    STRONGLY_AGREE = 1, "強く同意する"
    AGREE = 2, "同意する"
    NEUTRAL = 3, "どちらでもない"
    DISAGREE = 4, "同意しない"
    STRONGLY_DISAGREE = 5, "強く同意しない"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.IntegerField(choices=AnswerChoices.choices)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "回答"
        verbose_name_plural = "回答一覧"