from django import forms


class LoginUserForm(forms.Form):
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'id': 'floatingInput',
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'name@example.com',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'id': 'floatingPassword',
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Password',
            }
        )
    )
