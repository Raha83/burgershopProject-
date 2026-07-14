from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email_active_code=models.CharField(blank=True,verbose_name="کد فعالسازی حساب")
    avatar=models.ImageField(blank=True,upload_to='images/profiles',verbose_name="تصویر پروفایل")
 
    class Meta:
        verbose_name="کاربر" 
        verbose_name_plural="کاربران" 

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        else:
            return self.email
