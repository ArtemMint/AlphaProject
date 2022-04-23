from django import forms

from _db import models


class LoginUserForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = (
            'email',
            'password',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'id': 'floatingInput',
                    'class': 'form-control',
                    'type': 'email',
                    'placeholder': 'name@example.com',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'id': 'floatingPassword',
                    'class': 'form-control',
                    'type': 'password',
                    'placeholder': 'Password',
                }
            )
        }
