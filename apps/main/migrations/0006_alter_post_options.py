# Generated by Django 4.2.1 on 2023-05-30 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_post_title_alter_comment_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
    ]
