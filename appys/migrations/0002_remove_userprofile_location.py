# Generated by Django 3.2.24 on 2024-02-21 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
    ]
