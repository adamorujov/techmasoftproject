# Generated by Django 3.2.6 on 2021-08-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_pagemodel_corporative_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestionmodel',
            name='suggestion_direction',
            field=models.CharField(choices=[('L', 'Sol'), ('R', 'Sağ')], default='L', max_length=1),
        ),
    ]
