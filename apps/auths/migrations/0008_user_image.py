# Generated by Django 4.2.1 on 2023-06-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0007_remove_user_activation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
