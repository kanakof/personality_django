from django.db import models

# # Create your models here.

class Question(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Noanswer'),
    ]

    BLOODTYPE_CHOICES = (
        ('A', 'A型'),
        ('B', 'B型'),
        ('O', 'O型'),
        ('AB', 'AB型'),
    )

    name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    bloodtype = models.CharField(choices=BLOODTYPE_CHOICES, max_length=2)


class Answer(models.Model):
    QUESTION_CHOICES = [
        (1, '全く同意しない'),
        (2, 'あまり同意しない'),
        (3, 'どちらでもない'),
        (4, 'まあ同意する'),
        (5, 'とても同意する'),
    ]

    item1 = models.IntegerField(choices=QUESTION_CHOICES)
    item2 = models.IntegerField(choices=QUESTION_CHOICES)
    item3 = models.IntegerField(choices=QUESTION_CHOICES)
    item4 = models.IntegerField(choices=QUESTION_CHOICES)
    item5 = models.IntegerField(choices=QUESTION_CHOICES)
    item6 = models.IntegerField(choices=QUESTION_CHOICES)
    item7 = models.IntegerField(choices=QUESTION_CHOICES)
    item8 = models.IntegerField(choices=QUESTION_CHOICES)
    item9 = models.IntegerField(choices=QUESTION_CHOICES)
    item10 = models.IntegerField(choices=QUESTION_CHOICES)
    item11 = models.IntegerField(choices=QUESTION_CHOICES)
    item12 = models.IntegerField(choices=QUESTION_CHOICES)
    item13 = models.IntegerField(choices=QUESTION_CHOICES)
    item14 = models.IntegerField(choices=QUESTION_CHOICES)
    item15 = models.IntegerField(choices=QUESTION_CHOICES)
    item16 = models.IntegerField(choices=QUESTION_CHOICES)
    item17 = models.IntegerField(choices=QUESTION_CHOICES)
    item18 = models.IntegerField(choices=QUESTION_CHOICES)

