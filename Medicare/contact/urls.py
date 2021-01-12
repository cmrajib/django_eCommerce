from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('',views.contact,name='contact'),
    # path('profile/', views.user_profile, name='profile'),
]





