# Generated by Django 4.2.1 on 2023-06-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0025_remove_user_activation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/default.png', null=True, upload_to='avatar/'),
        ),
    ]
