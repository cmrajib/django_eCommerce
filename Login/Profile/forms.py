from django import forms
from django.contrib.auth.forms import UserChangeForm

from UserRegistration.models import User, Profile


class UserProfileChange(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','image')
        path = forms.CharField(required=False)

class ProfilePic(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image',]

from django.contrib.auth import get_user_model


class EditProfile(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('image', )