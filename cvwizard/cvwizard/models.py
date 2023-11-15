from datetime import date

from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "users_hoge"

    name = models.CharField(max_length=200)
    birthdate = models.DateField("date of birth")

    def save(self, *args, **kwargs):
        if self.birthdate > date.today():
            raise ValueError("Birthdate cannot be in the future")
        super().save(*args, **kwargs)
