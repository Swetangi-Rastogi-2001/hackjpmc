# Generated by Django 4.0.5 on 2022-06-12 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_userdata_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='link',
            field=models.CharField(default='https://wa.me/91', max_length=30),
        ),
    ]
