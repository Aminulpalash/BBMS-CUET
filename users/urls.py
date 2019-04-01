from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
#import accounts.urls
from users import views as users_views
from django.contrib.auth import views as auth_views

app_name="users"

urlpatterns = [
   url(r'^signup/$', users_views.signup, name='signup'),
   url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
   url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
