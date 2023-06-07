from django import forms

class Person(forms.Form):
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    paid_member = models.BooleanField()