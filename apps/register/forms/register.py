from django import forms

from _db import models


class RegisterUserForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = (
            'email',
            'password',
            # 'password2',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            # 'password2': forms.PasswordInput(
            #     attrs={
            #         'class': 'form-control',
            #     }
            # )
        }
