# Generated by Django 3.2.6 on 2021-09-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_auto_20210919_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='message_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Göndərilmə tarixi'),
        ),
    ]