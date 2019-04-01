from django.contrib.auth.models import AbstractUser
from django.db import models


blood_CHOICES = (
("B+", "B+"),
("A-", "A-"),
("A+","A+"),
("O+", "O+"),
("O-", "O-"),
)

gender_CHOICES = (
("Male", "Male"),
("Female", "Female"),
)



class CustomUser(AbstractUser):
    phone_number    = models.CharField(max_length=17, blank=False)
    university_name      = models.CharField(max_length=17, blank=False)
    blood_group     = models.CharField(max_length=32,choices=blood_CHOICES,default="B+")
    gender = models.CharField(max_length=32,choices=gender_CHOICES,default="Male")
    DayCount = models.IntegerField(default=120,blank=True)


    def __str__(self):
        return self.email