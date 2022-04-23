from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import views

from _db import models


class LoginUserView(views.LoginView):
    """Login user in site"""
    template_name = 'register/login.html'
    # redirect_authenticated_user = True

    def get(self, request):
        return render(
            self.request,
            self.template_name
        )

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(
            email=email,
            password=password,
        )
        context = {}
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(
                    self.request.GET.get('next', 'register:user_login'),
                )
            else:
                context['error_message'] = "User is not active."
        else:
            context['error_message'] = "Email or password not correct."

        return render(
            self.request,
            self.template_name,
            context,
        )


class RegisterUserView(generic.View):
    """Register new user view"""
    model = models.User
    template_name = 'register/register.html'

    def get(self, request):
        return render(
            self.request,
            self.template_name,
        )


class LogoutUserView(generic.View):
    template_name = 'register:user_login'
    """Logout current user"""
    def get(self, request):
        logout(request)
        return redirect(self.template_name)
