from django.db import models

# Create your models here.

class GenderChoices(models.TextChoices):
   male = 'M', '男性'
   female = 'F', '女性'
   other = 'O', 'その他'
   no_answer = 'N', '回答しない'

class BloodTypeChoices(models.TextChoices):
    A = 'A', 'A型'
    B = 'B', 'B型'
    AB = 'AB', 'AB型'
    O = 'O', 'O型'
    OTHER = 'OTHER', 'その他'

class User(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, default=GenderChoices.no_answer)
    blood_type = models.CharField(max_length=5, choices=BloodTypeChoices.choices, default=BloodTypeChoices.OTHER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー一覧"
    
    def __str__(self):
        return self.name
    