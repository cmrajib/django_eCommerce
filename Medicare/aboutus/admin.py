from django.contrib import admin


# Register your models here.

from aboutus.models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    list_display_links = ('name', 'phone', 'email')
    # list_filter = ('user__email','full_name','city')
    # list_editable = ('is_featured',)
    search_fields =('name', 'phone')
    list_per_page = 10




admin.site.register(Appointment, AppointmentAdmin)
# admin.site.register(Profile, CarAdmin)

