# Generated by Django 4.0.5 on 2022-06-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='above_knee_jaipur_foot',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='address',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='age',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='below_knee_jaipur_foot',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='caliper',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='cruthces',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='distribution_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='enrollment_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='hands',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='hearing_aids',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='knee_cap',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='landline_number',
            field=models.PositiveBigIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='ls_belt',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='mobile_number',
            field=models.PositiveBigIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='pincode',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='project',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='ratnanidhi_leg',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='sex',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='soft_collor',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='tricycle',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='wheelchair',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
