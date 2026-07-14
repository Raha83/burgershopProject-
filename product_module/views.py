from django.shortcuts import render
from django.views import View
from .models import Burger


class MenuView(View):
    def get(self,request):
        products=Burger.objects.filter(is_active=True)

        context={
            'products':products
        }
        return render(request,'product_module/menu.html',context)
