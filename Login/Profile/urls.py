from django.urls import path
from . import views

app_name = 'Profile'

urlpatterns = [
    path('',views.profile, name='profile'),
    path('change-profile/',views.user_change, name='user_change'),
    path('password/',views.pass_change, name='pass_change'),

    path('change-picture/',views.change_pro_pic, name='change_pro_pic'),
# To delete the previous profile picture it is required to install
# pip install django-cleanup
# In main project, settings.py, INSTALLED_APPS, write 'django_cleanup.apps.CleanupConfig',
]








#  http://localhost:8000/accounts/signup/
# http://localhost:8000/accounts/login/
# http://localhost:8000/accounts/logout/
# http://localhost:8000/profile
# http://localhost:8000/profile/password