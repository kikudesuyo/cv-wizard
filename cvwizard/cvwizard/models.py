from datetime import date

from django.db import models


# Create your models here.
class User(models.Model):
    last_name = models.CharField(verbose_name="名字", max_length=200)
    first_name = models.CharField(verbose_name="名前", max_length=200)
    birthdate = models.DateField(verbose_name="生年月日")

    def add(self, *args, **kwargs):
        if self.birthdate > date.today():
            raise ValueError("Birthdate cannot be in the future")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name
