from django.db import models
from users.models import CustomUser
blood_CHOICES = (
("B+", "B+"),
("A-", "A-"),
("A+","A+"),
("O+", "O+"),
("O-", "O-"),
)

class Patient(models.Model):
    patient_name = models.CharField(max_length=17, blank=False)
    patient_blood_group     = models.CharField(max_length=32,choices=blood_CHOICES,default="B+")
    patient_gender = models.CharField(max_length=32,default="Male")
    patient_hospital = models.CharField(max_length=32,default="CMC")

    def __str__(self):
        return self.patient_name

class ManageDonation(models.Model):
    donor_name = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    patient_name = models.ForeignKey(Patient,on_delete=models.CASCADE) 
    date = models.DateTimeField(auto_now_add=True)

    

