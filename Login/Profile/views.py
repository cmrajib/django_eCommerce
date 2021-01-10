import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from Profile.forms import UserProfileChange, ProfilePic, EditProfile
from UserRegistration.models import Profile


@login_required
def profile(request):
    single_profile = Profile.objects.get(id=request.user.id)
    return render(request, 'Profile/profile.html',context={'single_profile':single_profile})

@login_required
def user_change(request):
    current_user = request.user
    profile = Profile.objects.get(user=request.user)
    print (request.user.id)
    form = UserProfileChange(instance=profile)
    if request.method == 'POST':
        form = UserProfileChange(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=profile)

    return render(request, 'Profile/change_profile.html', context={'form':form})

@login_required
def pass_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    changed = False
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request,'Profile/pass_change.html', context={'form':form, 'changed':changed})

# Change existing profile picture
@login_required
def change_pro_pic(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfilePic(instance=request.user)
    if request.method == 'POST':
        form = ProfilePic(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Profile:profile'))
    return render(request,'Profile/pro_pic_add.html', context={'form':form})


# def user_edit(request):
#     if request.method == 'POST':
#         form = EditProfile(request.POST, instance=request.user)
#         if form.is_valid():
#             print('ok')
#             form.save()
#             if request.FILES.get('image', None) != None:
#                 try:
#                     os.remove(request.user.image.url)
#                 except Exception as e:
#                     print('Exception in removing old profile image: ', e)
#                 request.user.image = request.FILES['image']
#                 request.user.save()
#             return redirect('Profile:profile')
#     else:
#         form = EditProfile(instance=request.user)
#         return render(request, 'Profile/pro_pic_add.html', {'form': form})
