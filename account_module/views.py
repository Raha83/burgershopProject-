from django.views import View
from .forms import RegisterForm,LoginForm
from .models import User
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import login,logout
from utils.email_service import send_email


class RegisterView(View):
    def get(self,request):
        register_form=RegisterForm()

        context={
            'register_form':register_form
        }
        return render(request,'account_module/register_page.html',context)
    
    def post(self,request):
        register_form=RegisterForm(request.POST,request.FILES)
        
        if register_form.is_valid():
            user_fname=register_form.cleaned_data.get('first_name')
            user_lname=register_form.cleaned_data.get('last_name') 
            user_email=register_form.cleaned_data.get('email')
            user_avatar=register_form.cleaned_data.get('avatar')
            user_password=register_form.cleaned_data.get('password')
            user=User.objects.filter(email__iexact=user_email).exists()

            if user:
                register_form.add_error('email','این ایمیل قبلا در سایت ثبت شده است')
            else:
                new_user=User(first_name=user_fname,last_name=user_lname,email=user_email,
                              avatar=user_avatar,is_active=False,email_active_code=get_random_string(72))
                try:
                    validate_password(user_password)
                except ValidationError as e:
                    register_form.add_error('password', e)
                    context = {'register_form': register_form}
                    return render(request,'account_module/register_page.html',context)
                
                new_user.set_password(user_password)
                new_user.save()
                send_email('فعالسازی حساب کاربری',new_user.email,{'user':new_user},
                           'emails/active_account.html')
                return redirect(reverse('login_page'))
        context={
            'register_form':register_form
        }
        return render(request,'account_module/register_page.html',context)
    
class ActivateView(View):
    def get(self,request,email_active_code):
        user=User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            user.is_active=True
            user.email_active_code=get_random_string(72)
            user.save()
            return redirect(reverse('login_page'))
        else:
            return Http404('کاربر مورد نظر یافت نشد')
        
class LoginView(View):
    def get(self,request):
        login_form=LoginForm()

        context={
            'login_form':login_form
        }
        return render(request,'account_module/login_page.html',context)
    
    def post(self,request):
        login_form=LoginForm(request.POST)

        if login_form.is_valid():
            user_email=login_form.cleaned_data.get('email')
            user_pass=login_form.cleaned_data.get('password')
            user=User.objects.filter(email__iexact=user_email).first()
            if user:
                confirm_pass=user.check_password(user_pass)
                if confirm_pass:
                    if user.is_active == True:
                        login(request,user)
                        return redirect(reverse('index_page'))
                    else:
                        login_form.add_error('password','حساب کاربری شما فعال نیست')
                else:
                    login_form.add_error('password','اطلاعات وارد شده صحیح نمی‌باشد')
            else:
                raise Http404('کاربری با این مشخصات یافت نشد!')

            context={
                'login_form':login_form
            }
            return render(request,'account_module/login_page.html',context)

def LogoutView(request):
   logout(request) 
   return redirect(reverse('login_page'))