# Generated by Django 4.2.1 on 2023-05-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
