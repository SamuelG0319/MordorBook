# Generated by Django 4.1.3 on 2022-11-27 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_contactus_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
    ]