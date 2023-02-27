from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"sign__input", "placeholder":"Введите email"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class":"sign__input", "placeholder":"Введите пароль"})
    )


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    # password1 = "Введите пароль"
    # password2 = "Подтвердите пароль"

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            ]


