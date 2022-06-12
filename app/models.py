from django.db import models

class UserData(models.Model):
        
    project = models.CharField(max_length=100, default= None)
    enrollment_date = models.DateField(default= None)
    distribution_date = models.DateField(default= None)
    name = models.CharField(max_length=50, default= None)
    age= models.IntegerField(default= None)
    sex= models.CharField(max_length=20, default= None)
    address= models.CharField(max_length=100, default= None)
    pincode=models.CharField(max_length=6, default= None)
    mobile_number= models.PositiveBigIntegerField(default= None)
    landline_number= models.CharField(max_length=10, default= None)
    caliper=models.CharField(max_length=50, default= None)
    wheelchair = models.CharField(max_length=10, default= None)
    tricycle=models.CharField(max_length=10, default= None)
    cruthces=models.CharField(max_length=10, default= None)
    hearing_aids= models.CharField(max_length=10, default= None)
    hands=models.CharField(max_length=10, default= None)
    above_knee_jaipur_foot= models.CharField(max_length=20, default= None)
    below_knee_jaipur_foot= models.CharField(max_length=20, default= None)
    ratnanidhi_leg= models.CharField(max_length=20,default= None)
    ls_belt= models.CharField(max_length=10, default= None)
    knee_cap= models.CharField(max_length=10, default= None)
    soft_collor= models.CharField(max_length=10, default= None)
    maritial_status= models.CharField(max_length= 10, default= None, null= True)
    educational_background= models.CharField(max_length= 25, default= None, null= True)
    link= models.CharField(max_length= 30, default= 'https://wa.me/91')

    