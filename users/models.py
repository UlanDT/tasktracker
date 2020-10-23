from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Title(models.TextChoices):
    WD = "WD", "Web Designer"
    FD = "FD", "Frontend Developer"
    BD = "BD", "Backend Developer"
    PM = 'PM', "Product Manager"
    TL = "TL", "Team Lead"
    IOS = "IOS", "iOS Developer"
    AD = "AD", "Androind Developer"


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    title = models.CharField(max_length=3, choices=Title.choices)

    def __str__(self):
        return self.user.username
