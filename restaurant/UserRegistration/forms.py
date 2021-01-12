from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, forms

from UserRegistration.models import Profile, User



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


# Appling css class to the field and button
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'single-input'
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save', css_class='genric-btn success circle'))



class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('email','password1', 'password2',)

    # Appling css class to the field and button
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'single-input'
        # self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Create Account', css_class='genric-btn success circle'))



