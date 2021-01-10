from django.urls import path
from . import views

app_name = 'UserRegistration'

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
]










#  http://localhost:8000/accounts/signup/
# http://localhost:8000/accounts/login/
# http://localhost:8000/accounts/logout/
# http://localhost:8000/profile
# http://localhost:8000/profile/password