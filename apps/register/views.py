from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from register import forms


class BaseUserRegisterView(generic.View):
    form_class: forms = ''
    redirect_url: str = ''
    template_name: str = ''
    success_message: str = ''

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class}
        )

    def post(self, request):
        pass


class CreateUserView(BaseUserRegisterView):
    """Register new user view"""
    form_class = forms.CreateUserForm
    redirect_url = 'register:user_login'
    template_name = 'register/register.html'
    success_message = "Your profile was created successfully!"

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('email')
            form.save()
            return redirect(self.redirect_url)
        return render(
            request,
            self.template_name,
            {'form': form}
        )


class LoginUserView(BaseUserRegisterView):
    """ Login user view"""
    form_class = forms.LoginUserForm
    redirect_url = 'website:home_page'
    template_name = 'register/login.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request,
                username=email,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect(self.redirect_url)
        return render(
            request,
            self.template_name,
            {'form': form}
        )


class LogoutUserView(BaseUserRegisterView):
    """Logout user view"""
    redirect_url = 'website:home_page'

    def get(self, request):
        logout(request)
        return redirect(self.redirect_url)
