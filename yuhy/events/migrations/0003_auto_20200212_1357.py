# Generated by Django 3.0.3 on 2020-02-12 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200212_1339'),
    ]

    operations = [
        migrations.RemoveField('eventuser', 'country_id'),
    ]
