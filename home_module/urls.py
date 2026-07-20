from django.urls import path 
from . import views

urlpatterns=[
    path('',views.HomeView.as_view(),name='index_page'),
    path('about-us',views.AboutView.as_view(),name='about_us_page'),
    path('contact-us',views.ContactView.as_view(),name='contact_us_page')
]