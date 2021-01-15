from django import forms
from .models import *
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


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
        model = User
        exclude = [""]


class RegistrationYacht(forms.ModelForm):

    class Meta:
        model = Owner
        exclude = [""]


YachtFormset = forms.inlineformset_factory(Owner, Yacht,
exclude=[""], extra=1, can_delete=False, )


class ReservationYacht(forms.ModelForm):
    # pay_method = forms.ChoiceField(label='Способ оплаты')

    class Meta:
        model = Lease
        exclude = [""]
