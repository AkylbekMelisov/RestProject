from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Profile(models.Model):
    full_name = models.CharField(max_length=40)
    image = models.ImageField(blank=True)
    age = models.PositiveIntegerField()
    date_join = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name