from django import forms
from django.contrib.auth.models import User
from django.core import validators
from firstapp.models import UserProfileInfo

# #class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     number = forms.IntegerField()
#     botcatcher = forms.CharField(required=False,
#                                     widget=forms.HiddenInput,
#                                     validators=[validators.MaxLengthValidator(0)])

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

#setting it equal to the model in model.py
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
