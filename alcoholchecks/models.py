from django.db import models
from django.contrib.auth.models import User

class Info(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    CHOICES = (
        ("アルコール検知: 0.00mg", "0.00mg"),
        ("アルコール検知: 0.15mg未満", "0.15mg未満"),
        ("アルコール検知: 0.15mg以上", "0.15mg以上")
        )
    carnumbers = (
        ("6882", "6882"), ("2151", "2151"), ("2532", "2532"), ("5173", "5173"), ("5999", "5999"),
        ("386", "386"), ("783", "783"), ("2569", "2569"), ("777", "777"), ("3080", "3080")
    )
    alcohol = models.CharField(choices=CHOICES, max_length=20)
    carnumber = models.CharField(choices=carnumbers, max_length=20)

    def __str__(self):
        return self.alcohol
