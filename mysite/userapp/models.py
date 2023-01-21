from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    is_verificied = models.BooleanField(default=False)
    news = models.SmallIntegerField(default=0)
