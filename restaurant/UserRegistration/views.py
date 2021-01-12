from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from UserRegistration.forms import SignUpForm, ProfileForm
from UserRegistration.models import Profile

def home(request):
    return HttpResponse('Home')

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('UserRegistration:login'))

    return render(request,'UserRegistration/signup.html', context={'form': form})
def login_user(request):
    form = AuthenticationForm()

    form.fields['username'].widget.attrs['class'] = "single-input"
    form.fields['password'].widget.attrs['class'] = "single-input"


    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('UserRegistration:home'))
    return render(request,'UserRegistration/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You are logged out")
    return HttpResponseRedirect(reverse('UserRegistration:home'))



@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully')
            form = ProfileForm(instance=profile)

    return render( request, 'UserRegistration/change_profile.html', context={'form':form})
