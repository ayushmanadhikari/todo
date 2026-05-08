from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import Settings
import random
from django.utils import timezone, time
from datetime import timedelta

# Create your models here.
## custom user model with is_verified attribute
class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=10, blank=True)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.email
    

## otp module to generate and handle otp verification
class otpVerification(models.Model):
    user = models.OneToOneField(Settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    otp = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.otp = random.randint(1000, 9999)
        self.save()
        return self.otp
    
    def validate(self, submitted_otp):
        if (timezone.now() - self.created_at) < timedelta(minutes=10):
            if submitted_otp == self.otp:
                user_instance = self.user
                user_instance.is_verified = True
                user_instance.save()
                return True
        else: 
            return 'invalid otp!'
        
