from django.conf import settings


from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('UserRegistration.urls')),
    path('meals/' , include('meals.urls' , namespace='meals')),
    path('reserve_table/' , include('reservation.urls' , namespace='reservation')),
    path('about-us/' , include('aboutus.urls' , namespace='aboutus')),
    path('blog/' , include('blog.urls' , namespace='blog')),
    path('contact/' , include('contact.urls' , namespace='contact')),
    path('' , include('home.urls' , namespace='home')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Resturant Admin Panel"
admin.site.site_title = "Resturant App Admin "
admin.site.site_index_title = "Welcome To Resturant Admin Panel"