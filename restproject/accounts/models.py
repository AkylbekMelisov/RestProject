from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=40)
    image = models.ImageField(blank=True, null=True)
    age = models.PositiveIntegerField()
    date_join = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
