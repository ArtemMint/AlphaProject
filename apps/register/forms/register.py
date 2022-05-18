from django import forms

from _db import models


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            # 'user_name',
            'email',
            'password',
            # 'confirm',
        )
        widgets = {
            # 'user_name': forms.EmailInput(
            #     attrs={
            #         'class': 'form-control',
            #     }
            # ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            # 'confirm': forms.PasswordInput(
            #     attrs={
            #         'class': 'form-control',
            #     }
            # )
        }
