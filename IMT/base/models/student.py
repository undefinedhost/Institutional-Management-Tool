from django.db import models

class Student(models.Model):
    studentId = models.CharField(max_length = 15)
    rollNumber = models.IntegerField( )
    studentPhoto = models.ImageField(upload_to="studentphotos/", height_field=None, width_field=None, max_length=100)
    dateOfAdmission = models.DateField(auto_now=True, auto_now_add=True)