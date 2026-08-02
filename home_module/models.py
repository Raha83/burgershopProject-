from django.db import models

class Comment(models.Model):
    email=models.EmailField(verbose_name="ایمیل")
    text=models.TextField(max_length=500,verbose_name="متن پیام")

    class Meta:
        verbose_name='نظر'
        verbose_name_plural='نظرات'

    def __str__(self):
        return self.email
