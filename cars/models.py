from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    photo_url = models.TextField()
    price = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.SmallIntegerField()

    def __str__(self):
        return self.model
