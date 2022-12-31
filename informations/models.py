from django.db import models

class Information(models.Model):
    year = models.IntegerField(max_length=10)
    month = models.IntegerField(max_length=10)
    motouke = models.CharField(max_length=20)
    kouzi = models.CharField(max_length=20, default="")
    place = models.CharField(max_length=20)
    color_number = models.CharField(max_length=30)
    other = models.CharField(max_length=70)

    def __str__(self):
        return self.motouke
