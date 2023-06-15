from django.db import models
from django.utils import timezone

class Question(models.Model):
    body = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = "質問"
        verbose_name_plural = "質問一覧"


class AnswerChoices(models.IntegerChoices):
    STRONGLY_AGREE = 1, "とても同意する"
    AGREE = 2, "まあ同意する"
    NEUTRAL = 3, "どちらでもない"
    DISAGREE = 4, "あまり同意しない"
    STRONGLY_DISAGREE = 5, "全く同意しない"

class GenderChoices(models.IntegerChoices):
    FEMALE = 1, "女性"
    MALE = 2, "男性"
    NONE = 3, "無回答"

class BtypeChoices(models.IntegerChoices):
    A = 1, "A型"
    B = 2, "B型"
    O = 3, "O型"
    AB = 4, "AB型"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.IntegerField(choices=AnswerChoices.choices, default=AnswerChoices.NEUTRAL)
    genderchoices = models.IntegerField(choices= GenderChoices.choices, default= GenderChoices.NONE)
    btypechoice = models.IntegerField(choices=BtypeChoices.choices, default=BtypeChoices.A)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "回答"
        verbose_name_plural = "回答一覧"