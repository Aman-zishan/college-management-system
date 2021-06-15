

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


def __init__(self, user, *args, **kwargs):
    self.user = user
    super(LoginForm, self).__init__(*args, **kwargs)


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    # prevents students from creating fake teacher accounts to access/alter the DB ;)
    staff_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "cusat staff code",
                "class": "form-control",

            }
        ),required=False)


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))
    CHOICES = [('Student', 'Student'), ('Teacher', 'Teacher')]
    mode = forms.ChoiceField(widget=forms.RadioSelect(attrs={"id": "mode"}), choices=CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'firstname', 'email', 'password1', 'password2', 'mode')



