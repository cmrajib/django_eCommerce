from django.contrib import admin

from django.utils.html import format_html


# Register your models here.
from UserRegistration.models import User, Profile


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))

    thumbnail.short_description = 'Photo'






# Displaying email address from User model

    model = Profile

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field  = 'email'  #Allows column order sorting
    get_email.short_description = 'Email'  #Renames column head

    #Filtering on side - for some reason, this works
    #list_filter = ['user__email']
    # list_display_links = ('get_email')

# Displaying email address from User model









    list_display = ('get_email', 'thumbnail','full_name', 'phone','city', 'zipcode', 'country')
    list_display_links = ('get_email', 'thumbnail', 'full_name')
    list_filter = ('user__email','full_name','city')
    # list_editable = ('is_featured',)
    search_fields =('full_name', 'city','phone')
    list_per_page = 10




admin.site.register(User)
admin.site.register(Profile, CarAdmin)


