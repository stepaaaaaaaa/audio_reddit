# Generated by Django 4.2.1 on 2023-06-05 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0004_user_activation_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activation_code',
        ),
    ]
