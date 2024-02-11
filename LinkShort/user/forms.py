from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Links


class UserRegForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             label='Email')

    def __init__(self, *args, **kwargs):
        super(UserRegForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Name'
        }


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class LinkAddForm(forms.ModelForm):
    short = forms.SlugField(required=True, label='Short link')
    long = forms.CharField(required=True, label='Long link')

    class Meta:
        model = Links
        fields = ['short', 'long']