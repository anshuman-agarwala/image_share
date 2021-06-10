from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from .models import AppUser

class AppUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = UserCreationForm.Meta.fields + ('email' ,'first_name', 'last_name')
