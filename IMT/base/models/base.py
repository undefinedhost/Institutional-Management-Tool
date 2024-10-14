from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

#Fetching Choice Fields 
rl_category = [(rlcat, rlcat) for rlcat in settings.RELATIONSHIP_CHOICES]
religion_choices = [(rlch, rlch) for rlch in settings.RELIGION_CHOICES]
gender_choices = [(gd, gd) for gd in settings.GENDER_CHOICES]
doc_choices = [(doc,doc) for doc in settings.DOCUMENT_CHOICES]

class Address(models.Model):
    street_address = models.CharField(max_length=125)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return "Address Saved !"

class VerificationDocuments(models.Model):
    documentType = models.CharField(max_length = 20, choices= doc_choices)
    documentUpload = models.FileField(upload_to="verifydocs/")
    

class RelationshipContact(models.Model):

    rlname = models.CharField(max_length = 50)
    rlCategory = models.CharField(max_length = 25, choices= rl_category)
    rlContact = models.IntegerField(max_length= 10, blank= False, null= False)
    rladdress = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.rlCategory} information saved !"
    
    

class Person(models.Model):
    
    fullname = models.CharField(max_length = 50)
    dateofbirth = models.DateField(auto_now= False, auto_now_add= False)
    gender = models.CharField(max_length = 25, choices= gender_choices)
    contactnumber = models.CharField(max_length= 18, blank= True, null= True)
    emailaddress = models.EmailField(max_length= 50, blank= True, null= True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    rlcontactinfo = models.ForeignKey(RelationshipContact, on_delete=models.CASCADE)
    documents = models.ManyToManyField(VerificationDocuments, related_name="verification_docs") 
    religion = models.CharField(max_length = 25, choices=religion_choices)
    caste = models.CharField(max_length = 30)
    

    class Meta:
        abstract = True