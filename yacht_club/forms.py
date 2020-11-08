from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Users
        exclude = [""]


class LeaseForm(forms.ModelForm):

    class Meta:
        model = Lease
        exclude = [""]


class LoginForm(forms.ModelForm):

    class Meta:
        model = Users
        exclude = [""]


class RegistrationYacht(forms.ModelForm):
    class Meta:
        model = Yacht
        exclude = [""]


class RegistrationOwner(forms.ModelForm):
    class Meta:
        model = Owner
        exclude = [""]