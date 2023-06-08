from django.db import models

# # Create your models here.

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('N', 'Noanswer'),
)

BLOODTYPE_CHOICES = (
    ('A', 'A型'),
    ('B', 'B型'),
    ('O', 'O型'),
    ('AB', 'AB型'),
)


class Questions(models.Model):
    name = models.CharField(max_length=100)
    gender = models.ChoiceField(choices=GENDER_CHOICES, max_length=1)
    bloodtype = models.ChoiceField(choices=BLOODTYPE_CHOICES, max_length=1)