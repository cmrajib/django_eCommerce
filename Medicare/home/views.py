from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from UserRegistration.models import User
from aboutus.models import Appointment
from blog.models import Post


def home(request):
    posts = Post.objects.order_by('-created')

    doctors = User.objects.filter(user_type='Doctor')
    # user = User.objects.filter(email=user)
    if request.method == "POST":
        if request.user.is_authenticated:
            name = request.user.full_name
            email = request.user.email
            phone = request.user.phone
            user_id = request.user.id
            message = request.POST['message']
            print(phone, email, name, message, user_id)

            Appointment.objects.create(name=name, email=email,
                                       phone=phone, usermessage=message,user_id=user_id)
            # messages.info(request, "Apoinment saved")
        else:
            return redirect('UserRegistration:login')


    context = {
        'posts': posts,
        'doctors': doctors,
    }
    return render(request, 'home/home.html', context)