from django.db import models

class Burger(models.Model):
    name=models.CharField(max_length=100,verbose_name="نام محصول")
    price=models.IntegerField(verbose_name="قیمت محصول")
    image=models.ImageField(upload_to="images/products",verbose_name="تصویر محصول")
    short_description=models.CharField(max_length=300,null=True,verbose_name="توضیحات محصول")
    is_active=models.BooleanField(verbose_name='موجود/غیرموجود')
    
    class Meta:
        verbose_name="محصول"
        verbose_name_plural="محصولات"

    def __str__(self):
        return self.name

