from django.shortcuts import redirect, render
from django.views.generic import FormView, CreateView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.

from accounts.forms import LoginForm, UserRegisterForm

from accounts.models import User


class LoginView(FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"

    def form_valid(self, form):
        data = form.cleaned_data  # {"password":"admin", "email":"admin@gmail.com"}
        # cleaned_data хранилище данных из формы в виде dict
        print(data)
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("index")
            return HttpResponse("Ваш аккаунт не активен!")
        return HttpResponse("<b>Введенные Вами данные некорректны!</b>")


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")


class UserRegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = UserRegisterForm
    model = User
    success_url = reverse_lazy("login")


class RegisterDoneView(TemplateView):
    template_name = "accounts/register_done.html"

