# Generated by Django 4.2.1 on 2023-06-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0013_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/'),
        ),
    ]
