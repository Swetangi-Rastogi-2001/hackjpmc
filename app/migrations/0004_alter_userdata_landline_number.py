# Generated by Django 4.0.5 on 2022-06-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_userdata_landline_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='landline_number',
            field=models.CharField(default=None, max_length=10),
        ),
    ]