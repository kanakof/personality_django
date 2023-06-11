from django.db import models

# Create your models here.

class GenderChoices(models.TextChoices):
   ('M', '男性'),
   ('F', '女性'),
   ('O', 'その他'),
   ('N', '回答しない')

class BloodTypeChoices(models.TextChoices):
    ('A', 'A型'),
    ('B', 'B型'),
    ('AB', 'AB型'),
    ('O', 'O型'),
    ('OTHER', 'その他')

class User(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, default=GenderChoices.N)
    blood_type = models.CharField(max_length=5, choices=BloodTypeChoices.choices, default=BloodTypeChoices.OTHER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー一覧"
    
    def __str__(self):
        return self.name