from django.db import models
from account_module.models import User
from product_module.models import Burger

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    is_paid=models.BooleanField(verbose_name='پرداخت شده/نشده')
    payment_date=models.DateField(null=True,blank=True,verbose_name='تاریخ پرداخت')

    def calculate_total_price(self):
        total_amount=0
        if self.is_paid:
            for detail in self.orderdetail_set.all():
                total_amount += detail.final_price * detail.count
                return total_amount
        else:
            for detail in self.orderdetail_set.all():
                total_amount += detail.product.price * detail.count
            return total_amount
            
    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name="سبد خرید کاربر"
        verbose_name_plural="سبد خرید کاربران"

class OrderDetail(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='سفارش')
    product=models.ForeignKey(Burger,on_delete=models.CASCADE,blank=True,verbose_name='محصول')
    count=models.IntegerField(blank=True,verbose_name='تعداد محصول')
    final_price=models.IntegerField(null=True,blank=True,verbose_name='قمیت نهایی تک محصول')
 
    def get_total_price(self):
        total_price=self.product.price * self.count
        return total_price
    
    def __str__(self):
        return str(self.order)
    
    class Meta:
        verbose_name="جزئیات سبد خرید"
        verbose_name_plural="جزئیات"
