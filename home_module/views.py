from django.shortcuts import render,redirect
from django.views import View
from product_module.models import Burger
from site_module.models import SiteSetting,FooterCat,Slider
from .models import Comment
from .forms import CommentForm


class HomeView(View):
    def get(self,request):
        product=Burger.objects.filter(is_active=True)[0:4]
        popular_product=Burger.objects.filter(is_active=True,is_popular=True)[0:2]
        site_setting=SiteSetting.objects.filter(is_main_setting=True).first()
        sliders=Slider.objects.filter(is_active=True)
        comment_form=CommentForm()
        comments=Comment.objects.filter().order_by('-created_at')
        
        context={
            'burgers':product,
            'popular_burgers':popular_product,
            'site_setting':site_setting,
            'sliders':sliders,
            'comment_form':comment_form,
            'comments':comments
        }
        return render(request,'home_module/index.html',context)
    def post(self,request):
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save()
            return redirect('index_page')
            comment_form=CommentForm()

        context={
            'comment_form':comment_form
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