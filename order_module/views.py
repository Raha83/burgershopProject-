from django.shortcuts import render
from django.template.loader import render_to_string
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

@login_required
def change_order_quantity(request):
    detail_id=request.GET.get('detail_id')
    state=request.GET.get('state')
    
    if detail_id is None or state is None:
        return JsonResponse({
            'status':'not_found_detail_id_state'
        })
    
    current_detail=OrderDetail.objects.filter(id=detail_id,order__is_paid=False,order__user_id=request.user.id).first()
    if current_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })
    
    if state == 'increase':
        current_detail.count +=1
        current_detail.save()
    elif state == 'decrease':
        if current_detail.count == 1:
            current_detail.delete()
        else:
            current_detail.count -=1
            current_detail.save()
    else:
        return JsonResponse({
            'status':'invalid_state'
        })

    current_order,created=Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,user_id=request.user.id)
    total_amount=current_order.calculate_total_price()
    context={
        'current_order':current_order,
        'total_amount':total_amount
    }
    return JsonResponse({
        'status':'success',
        'body':render_to_string('order_module/user_basket.html',context)
    })