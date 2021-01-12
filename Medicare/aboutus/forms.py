from django import forms

from aboutus.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'name',
            'phone',
            'email',
            'usermessage'

        ]

