# Generated by Django 4.0.6 on 2023-05-04 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0011_house_likes_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='property_id',
            new_name='house_id',
        ),
    ]
