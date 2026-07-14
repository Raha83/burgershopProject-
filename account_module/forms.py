from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    first_name=forms.CharField(
        label='نام',
        required=False
    )
    last_name=forms.CharField(
        label='نام ‌خانوادگی',
        required=False
    )
    email=forms.EmailField(
        label='ایمیل'
    )
    avatar=forms.ImageField(
        label='تصویر پروفایل',
        widget=forms.FileInput(),
        required=False
    )
    password=forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput() 
    )
    confirm_pass=forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput()
    )
 
    def clean_confirm_pass(self):
        password=self.cleaned_data.get('password')
        confirm_pass=self.cleaned_data.get('confirm_pass')

        if password == confirm_pass:
            return confirm_pass
        raise ValidationError('رمز عبور و تکرار آن با یکدیگر مطابقت ندارند')
    
class LoginForm(forms.Form):
    email=forms.EmailField(
        label='ایمیل'
    )
    password=forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput()
    )