from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
         model=Comment
         fields=['first_name','last_name','text']

         widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control valid',
                'placeholder': 'نام'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control valid',
                'placeholder': 'نام خانوادگی'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'متن پیام',
                'rows': 9,
                'cols':30
            })
         }