from django.db import models

class SiteSetting(models.Model):
    logo=models.ImageField(upload_to="images/site_setting",verbose_name="لوگو سایت")
    url=models.URLField(verbose_name="نشانی سایت")
    phone=models.CharField(null=True,blank=True,verbose_name="شماره تماس")
    email=models.EmailField(null=True,blank=True,verbose_name="ایمیل")
    address=models.CharField(max_length=100,verbose_name='آدرس شعبه اصلی')
    introduction_text=models.CharField(null=True,blank=True,max_length=300,verbose_name="معرفی سایت")
    about_us_text=models.TextField(null=True,blank=True,verbose_name="متن درباره‌ی ما")
    intro_image=models.ImageField(null=True,upload_to='images/site_setting',verbose_name="تصویر معرفی سایت")
    copy_right=models.TextField(max_length=500,verbose_name="متن کپی‌رایت")
    is_main_setting=models.BooleanField(verbose_name="تنظیمات اصلی")

    class Meta:
        verbose_name="تنظیمات سایت"
        verbose_name_plural="تنظیمات"

    def __str__(self):
        return self.url

class FooterCat(models.Model):
    name=models.CharField(max_length=100,verbose_name="شهر")

    class Meta:
        verbose_name="دسته‌بندی فوتر"
        verbose_name_plural="دسته‌بندی‌ها"

    def __str__(self):
        return self.name
    
class FooterLink(models.Model):
    category=models.ForeignKey(FooterCat,on_delete=models.CASCADE,verbose_name="شعبه")
    address=models.CharField(max_length=100,null=True,verbose_name="آدرس شعبه")
    website=models.URLField(verbose_name="وبسایت شعبه")
    phone=models.CharField(null=True,verbose_name="شماره تماس شعبه")

    class Meta:
        verbose_name="لینک فوتر"
        verbose_name_plural="لینک‌ها"

    def __str__(self):
        return self.address
    
class Slider(models.Model):
    title=models.CharField(max_length=100,verbose_name="عنوان اسلایدر")
    name=models.CharField(max_length=100,verbose_name="نام محصول")
    short_description=models.CharField(max_length=300,verbose_name="توضیحات کوتاه")
    image=models.ImageField(upload_to='images/sliders',verbose_name="تصویر اسلایدر")
    is_active=models.BooleanField(verbose_name="فعال/غیرفعال")

    class Meta:
        verbose_name="اسلایدر"
        verbose_name_plural="اسلایدر‌ها"

    def __str__(self):
        return self.title