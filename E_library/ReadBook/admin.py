from django.contrib import admin

# Register your models here.
from ReadBook.models import UserInfo, Book

admin.site.register(UserInfo)
admin.site.register(Book)