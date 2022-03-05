from django import forms
from app_shops.models import UserAccount


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'
