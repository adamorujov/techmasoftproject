# Generated by Django 3.2.6 on 2021-08-28 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_alter_pagemodel_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagemodel',
            name='banner_image',
        ),
        migrations.RemoveField(
            model_name='pagemodel',
            name='contact_image',
        ),
    ]
