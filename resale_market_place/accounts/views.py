from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accounts.forms import SignUpForm, ProfileForm
from accounts.models import Profile


def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('accounts:login'))

    return render(request,'accounts/register.html', context={'form': form})



def login_user(request):
    form = AuthenticationForm()

    # form.fields['username'].widget.attrs['class'] = "single-input"
    # form.fields['password'].widget.attrs['class'] = "single-input"


    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('products:product_list'))
    return render(request,'accounts/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You are logged out")
    return HttpResponseRedirect(reverse('accounts:login'))



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

    return render( request, 'accounts/profile-update.html', context={'form':form})
