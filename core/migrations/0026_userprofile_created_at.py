# Generated by Django 4.0.6 on 2023-05-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_userprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
