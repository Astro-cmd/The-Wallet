from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, null= False)
    phone = models.CharField(max_length=15, blank = True, null = True)
    address = models.CharField(max_length=255, blank = True, null = True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'