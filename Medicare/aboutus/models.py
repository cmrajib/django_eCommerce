from django.db import models

# Create your models here.
from UserRegistration.models import User


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True,blank=True)
    phone = models.CharField(max_length=15, null=True,blank=True)
    email = models.EmailField()
    usermessage = models.TextField()




    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return self.email