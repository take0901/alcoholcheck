from django.db import models

class Information(models.Model):
    CHOICES = (
        ("1", "1"),("2", "2"),
        ("3", "3"), ("4", "4"),
        ("5", "5"), ("6", "6"),
        ("7", "7"),("8", "8"),
        ("9", "9"),("10", "10"),
        ("11", "11"), ("12", "12")
    )
    year = models.CharField(max_length=10)
    month = models.CharField(max_length=10, choices=CHOICES)
    motouke = models.CharField(max_length=20)
    kouzi = models.CharField(max_length=20, default="")
    place = models.CharField(max_length=20)
    color_number = models.CharField(max_length=30)
    other = models.CharField(max_length=70)

    def __str__(self):
        return self.motouke
