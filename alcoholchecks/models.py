from django.db import models
from users.models import User
from alcoholcheck.settings import name, name2

class Info(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    CHOICES = (
        ("アルコール検知: 0.00mg", "0.00mg"),
        ("アルコール検知: 0.15mg未満", "0.15mg未満"),
        ("アルコール検知: 0.15mg以上", "0.15mg以上")
        )
    names = (
        (name, name),
        (name2, name2)
    )
    ways = (
        ('対面', '対面'),
        ('ビデオ通話', 'ビデオ通話')
    )
    carnumbers = tuple(User.objects.values_list("carnumber", "carnumber"))
    alcohol = models.CharField(choices=CHOICES, max_length=20)
    carnumber = models.IntegerField(choices=carnumbers)
    varified_by = models.CharField(max_length=10, choices=names)
    how_to = models.CharField(max_length=20, choices=ways)

    def __str__(self):
        return self.alcohol
