# Generated by Django 4.2.1 on 2023-05-30 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
