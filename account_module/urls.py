from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.RegisterView.as_view(),name='register_page'),
    path('active-account/<email_active_code>',views.ActivateView.as_view(),name='active_account'),
    path('login/',views.LoginView.as_view(),name='login_page'),
    path('logout/',views.LogoutView,name='logout_page')
]