from django.db import models

# Create your models here.
class Owner(models.Model):
    Owner_id = models.AutoField
    Owner_firstname = models.CharField(max_length=60)
    Owner_lastname = models.CharField(max_length=60)
    Owner_address = models.CharField(max_length=600)
    Owner_email = models.CharField(max_length=100)
    Owner_password = models.CharField(max_length=32)
    Owner_dob = models.DateField()
    Owner_mobileno = models.CharField(max_length=10)
    Owner_gender = models.CharField(max_length=15)
    Owner_license =  models.ImageField(upload_to='img/Owner_License/')
    Owner_agency = models.CharField(max_length=100)
    isOwner = models.BooleanField(default=True)

    def __str__(self):
        return self.Owner_email + ": " + str(self.Owner_license)