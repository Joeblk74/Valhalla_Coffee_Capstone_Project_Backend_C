from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Coffee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flavor = models.CharField(max_length=50)
    origin = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    price = models.IntegerField()