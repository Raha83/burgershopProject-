from django.db import models
from django.utils.timezone import now
from jalali_date import date2jalali

class Comment(models.Model):
    first_name=models.CharField(null=True,max_length=100,verbose_name='نام')
    last_name=models.CharField(null=True,max_length=100,verbose_name='نام خانوادگی')
    text=models.TextField(max_length=500,verbose_name="متن پیام")
    created_at=models.DateTimeField(auto_now_add=True,editable=False,verbose_name='تاریخ ایجاد')
    
    class Meta:
        verbose_name='نظر'
        verbose_name_plural='نظرات'

    def get_jalali_date(self):
        return date2jalali(self.created_at)

    def get_full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

    def __str__(self):
        return self.get_full_name()
