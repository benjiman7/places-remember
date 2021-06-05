from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    photo = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
