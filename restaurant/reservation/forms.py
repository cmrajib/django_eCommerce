from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.forms import DateInput

from .models import Reservation


# This is for Date Picker
class DateInput(forms.DateInput):
    input_type = 'date'

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        widgets = {
            'Date': DateInput(),
        }