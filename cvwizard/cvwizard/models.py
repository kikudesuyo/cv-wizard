from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField("date of birth")

    def __str__(self):
        return self.name
