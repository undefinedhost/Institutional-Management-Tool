from django.db import models

class Staff(models.Model):
    # staff category choice
    staffId = models.CharField(max_length = 13)
    photo = models.ImageField(upload_to="staffphotos/", height_field=None, width_field=None, max_length=100)
    dateOfJoining = models.DateField(auto_now=True, auto_now_add=True)
    salaryInfo = models.IntegerField()
    bankInfo = models.ForeignKey("BankInformation", on_delete=models.CASCADE)
    #highestQualification choice fields
    certificates = models.FileField(upload_to="staffcerts/")
    #specialization : categorized activation / or maybe null
    #employment type choice field
       
class BankInformation(models.Model):
    accountNumber = models.IntegerField()
    ifscCode = models.CharField(max_length = 15)
    accountName = models.CharField(max_length = 15)