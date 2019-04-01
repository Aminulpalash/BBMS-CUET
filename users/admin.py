# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','blood_group',]
    fieldsets = (
(None, {'fields': ('username', 'email', 'password','first_name','last_name',)}),
('Other info', {'fields': ('phone_number','university_name','blood_group','DayCount','gender',)}),
('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active',)}),
)

admin.site.register(User)
admin.site.register(CustomUser, CustomUserAdmin)