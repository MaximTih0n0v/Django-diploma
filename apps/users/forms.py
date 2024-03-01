from django import forms
from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm,
                                       UserChangeForm)
from apps.users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "last_name",
            "first_name",
            "patronymic",
            "username",
            "email",
            "phone",
            "password1",
            "password2",
        )

    last_name = forms.CharField()
    first_name = forms.CharField()
    patronymic = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "last_name",
            "first_name",
            "patronymic",
            "username",
            "email",
            "phone",
        )

    image = forms.ImageField(required=False)
    last_name = forms.CharField()
    first_name = forms.CharField()
    patronymic = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()


