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
    month = models.ForeignKey(Month, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    CHOICES = (
        ("アルコール検知なし", "あり"),
        ("アルコール検知なし", "なし")
        )
    alcohol = models.CharField(choices=CHOICES, max_length=20,null=True)

    def __str__(self):
        return self.alcohol
