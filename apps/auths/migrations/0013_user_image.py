# Generated by Django 4.2.1 on 2023-06-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0012_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
