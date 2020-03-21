
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name="home"),
    path('about', index, name="about"),
    path('account_signup', index, name="account_signup"),
    path('account_login', index, name="account_login"),
]