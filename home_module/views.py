from django.shortcuts import render
from django.views import View
from product_module.models import Burger
from site_module.models import SiteSetting,FooterCat,Slider


class HomeView(View):
    def get(self,request):
        product=Burger.objects.filter(is_active=True)[0:4]
        popular_product=Burger.objects.filter(is_active=True,is_popular=True)[0:2]
        site_setting=SiteSetting.objects.filter(is_main_setting=True).first()
        sliders=Slider.objects.filter(is_active=True)
        
        context={
            'burgers':product,
            'popular_burgers':popular_product,
            'site_setting':site_setting,
            'sliders':sliders
        }
        return render(request,'home_module/index.html',context)
    
def site_header_component(request):
    site_setting=SiteSetting.objects.filter(is_main_setting=True).first()

    context={
        'site_setting':site_setting
    }
    return render(request,'shared/header_component.html',context)

def site_footer_component(request):
    site_setting=SiteSetting.objects.filter(is_main_setting=True).first()
    footer_category=FooterCat.objects.all()
    
    context={
        'site_setting':site_setting,
        'footer_category':footer_category
    }
    return render(request,'shared/footer_component.html',context)

class AboutView(View):
    def get(self,request):
        site_setting=SiteSetting.objects.filter(is_main_setting=True).first()

        context={
            'site_setting':site_setting
        }
        return render(request,'home_module/about_us.html',context)
    
class ContactView(View):
    def get(self,request):
        site_setting=SiteSetting.objects.filter(is_main_setting=True).first()

        context={
            'site_setting':site_setting
        }
        return render(request,'home_module/contact_us.html',context)