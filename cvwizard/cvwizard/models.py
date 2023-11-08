from django.db import models


# Create your models here.
class PersonalInfomation(models.Model):
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name
