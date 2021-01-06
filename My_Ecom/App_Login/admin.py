from django.contrib import admin

# Register your models here.


from App_Login.models import Profile, User


admin.site.register(Profile)
admin.site.register(User)