from django.db import models
from django.contrib.auth.models import User

class Month(models.Model):
    CHOICES = (
        ("1月", "1月"),("2月", "2月"),
        ("3月", "3月"), ("4月", "4月"),
        ("5月", "5月"), ("6月", "6月"),
        ("7月", "7月"),("8月", "8月"),
        ("9月", "9月"),("10月", "10月"),
        ("11月", "11月"), ("12月", "12月")
    )
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    month = models.CharField(max_length=10, choices=CHOICES,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.month

class Info(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.PROTECT)
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
