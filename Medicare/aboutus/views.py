from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from UserRegistration.models import User
from aboutus.forms import AppointmentForm
from aboutus.models import Appointment


def home(request):
    doctors = User.objects.filter(user_type='Doctor')

    if request.method == "POST":
        if request.user.is_authenticated:
            name = request.user.full_name
            email = request.user.email
            phone = request.user.phone
            user_id = request.user.id
            message = request.POST['message']
            print(phone, email, name, message, user_id)

            Appointment.objects.create(name=name, email=email,
                                       phone=phone, usermessage=message, user_id=user_id)
            # messages.info(request, "Apoinment saved")
        else:
            return redirect('UserRegistration:login')

    context = {
        'doctors': doctors,

    }

    return render(request,'aboutus/aboutus.html', context)