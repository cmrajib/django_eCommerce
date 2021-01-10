from django.urls import path
from . import views

app_name = 'ReadBook'

urlpatterns = [
    path('', views.loadBook, name="premiumbook"),
    path('addbook/', views.addBook, name="addbook"),
    path('description/<int:bid>/', views.bookDescription, name='description'),
    path('delete/<int:bid>/', views.deleteBook, name='deletebook'),
]

