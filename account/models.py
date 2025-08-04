from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # this is user where i add onetoonefield relationship where one user one profile
    phone_number = models.CharField(max_length=10) # in built in user model there has no phone number fiels so i add one

    def __str__(self):
        return self.user.get_username()
