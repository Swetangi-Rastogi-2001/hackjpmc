import os

from app.models import UserData
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackjpmc.settings')

import django
django.setup()

import pandas as pd
import datetime
from datetime import date

def populate():
    df= pd.read_csv('Book1.csv')
    
    for i in range(0,df.shape[0]):
        usd = UserData.objects.get_or_create(
            project = df.iloc[i,0],
            enrollment_date = datetime.datetime.strptime(df.iloc[i,1], '%Y/%m/%d'),
            distribution_date = date.today(),
            name = df.iloc[i,3],
            age= df.iloc[i,4],
            sex= df.iloc[i,5],
            address= df.iloc[i,6],
            pincode= df.iloc[i,7],
            mobile_number= df.iloc[i,8],
            landline_number= df.iloc[i,9],
            caliper= df.iloc[i,10],
            wheelchair = df.iloc[i,11],
            tricycle= df.iloc[i,12],
            cruthces= df.iloc[i,13],
            hearing_aids= df.iloc[i,14],
            hands= df.iloc[i,15],
            above_knee_jaipur_foot= df.iloc[i,16],
            below_knee_jaipur_foot= df.iloc[i,17],
            ratnanidhi_leg= df.iloc[i,18],
            ls_belt= df.iloc[i,19],
            knee_cap= df.iloc[i,20],
            soft_collor= df.iloc[i,21]   
        )[0]
    

if __name__== '__main__':
    print("Population started!")
    populate()
    print("Population Complete!")