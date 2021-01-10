from django.contrib import admin

from django.utils.html import format_html


# Register your models here.
from UserRegistration.models import User, Profile


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail','full_name', 'phone','city', 'zipcode', 'country')
    list_display_links = ('id','thumbnail', 'full_name')
    list_filter = ('full_name','city')
    # list_editable = ('is_featured',)
    search_fields =('full_name', 'city','phone')
    list_per_page = 10

admin.site.register(User)
admin.site.register(Profile, CarAdmin)


