from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView

from _db import models
from register import forms


class LoginUserView(generic.View):
    template_name = 'register/login.html'
    login_redirect = 'website:home_page'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {}
        )

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=email,
            password=password,
        )
        if user is not None:
            login(request, user)
            return redirect(self.login_redirect)
        return render(
            request,
            self.template_name,
            {}
        )


class LogoutUserView(generic.View):
    logout_redirect = 'website:home_page'

    def get(self, request):
        logout(request)
        return redirect(self.logout_redirect)




class RegisterUserView(generic.CreateView):
    """Register new user view"""
    form_class = forms.RegisterUserForm
    success_url = reverse_lazy('sign-in/')
    template_name = 'register/register.html'
    success_message = "Your profile was created successfully!"

