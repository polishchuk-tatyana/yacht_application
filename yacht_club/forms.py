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
        model = Owner
        exclude = [""]


YachtFormset = forms.inlineformset_factory(Owner, Yacht,
fields=("type", "model", 'max_human', 'cabin', 'year', 'length', 'motor', 'club', 'manufacturer', 'paid', 'owner'),
exclude=[""], extra=1, can_delete=False, )


class ReservationYacht(forms.ModelForm):
    pay_method = forms.ChoiceField(label='Способ оплаты')

    class Meta:
        model = Lease
        exclude = [""]
