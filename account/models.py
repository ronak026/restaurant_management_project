from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # Links to built-in user
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\+?\d{10,15}$",
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
            )
        ],
        help_text="Enter phone number in international format (e.g., +919876543210)",
    )

    def __str__(self):
        return self.user.get_full_name()
