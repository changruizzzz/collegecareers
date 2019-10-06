from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Socials(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    avatar = models.CharField(max_length=2048)
