# Generated by Django 3.1.2 on 2023-06-28 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='price',
        ),
    ]
