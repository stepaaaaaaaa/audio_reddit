# Generated by Django 4.2.1 on 2023-05-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_comment_content_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(upload_to='audio_posts'),
        ),
    ]
