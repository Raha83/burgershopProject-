from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,JsonResponse
from product_module.models import Burger
from order_module.models import Order,OrderDetail


def addProductToOrder(request:HttpRequest):
    product_id=int(request.GET.get('product_id'))
    product_count=int(request.GET.get('product_count'))

    if product_count <1:
        return JsonResponse({
                'status':'invalid_count',
                'icon':'warning',
                'text':'مقدار وارد شده غیرمعتبر است',
                'confirm_button_text':'متوجه شدم'
            })
    else:
        product=Burger.objects.filter(id=product_id,is_active=True).first()
        if product is not None:
            if request.user.is_authenticated:
                current_order,created=Order.objects.get_or_create(user_id=request.user.id,is_paid=False)
                current_detail=current_order.orderdetail_set.filter(product_id=product_id).first()
                if current_detail is not None:
                    current_detail.count += product_count
                    current_detail.save()
                else:
                    new_detail=OrderDetail(order_id=current_order.id,product_id=product_id,count=product_count)
                    new_detail.save()
                context={
                    'current_order':current_order
                }
                return JsonResponse({
                    'status':'success',
                    'icon':'success',
                    'text':'محصول با موفقیت به سبد خرید اضافه شد',
                    'confirm_button_text':'مشاهده سبد خرید'
                      })
            else:
               return JsonResponse({
                   'status':'not_auth',
                   'icon':'error',
                   'text':'برای سفارش ابتدا می بایست لاگین شوید',
                   'confirm_button_text':'انتقال به صفحه لاگین'
                   })  
        else:
            return JsonResponse({
                 'status':'invalid_product',
                 'icon':'warning',
                 'text':'محصول با این مشخصات یافت نشد',
                 'confirm_button_text':'متوجه شدم'
                   })

@login_required        
def userBasketView(request:HttpRequest):
    current_order,created=Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,user_id=request.user.id)
    context={
        'current_order':current_order
    }
    return render(request,'order_module/user_basket.html',context)