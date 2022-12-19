from django.db import models
from users.models import User

class Info(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    CHOICES = (
        ("アルコール検知: 0.00mg", "0.00mg"),
        ("アルコール検知: 0.15mg未満", "0.15mg未満"),
        ("アルコール検知: 0.15mg以上", "0.15mg以上")
        )
    carnumbers = tuple(User.objects.values_list("carnumber", "carnumber"))
    alcohol = models.CharField(choices=CHOICES, max_length=20)
    carnumber = models.IntegerField(choices=carnumbers)

    def __str__(self):
        return self.alcohol
