# Generated by Django 3.2.11 on 2022-01-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='club_name',
            field=models.CharField(choices=[('Select', 'Select'), ('SWC', 'SWC'), ('CODING CLUB', 'CODING CLUB'), ('AERO CLUB', 'AERO CLUB'), ('ASTRO CLUB', 'ASTRO CLUB'), ('CA CLUB', 'CA CLUB'), ('EE CLUB', 'EE CLUB'), ('PRAKRITI CLUB', 'PRAKRITI CLUB'), ('FNC CLUB', 'FNC CLUB'), ('ROBOTICS CLUB', 'ROBOTICS CLUB'), ('ED CLUB', 'ED CLUB'), ('UG CLUB', 'UG CLUB'), ('ALCHER CLUB', 'ALCHER CLUB'), ('TECHNICHE CLUB', 'TECHNICHE CLUB'), ('SAIL CLUB', 'SAIL CLUB'), ('AI CLUB', 'AI CLUB'), ('CCD CLUB', 'CCD CLUB'), ('OTHER CLUB', 'OTHER CLUB')], default='Not A Club Member', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='club_status',
            field=models.BooleanField(default=0),
        ),
    ]