# Generated by Django 4.0.6 on 2023-05-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_properties_owner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]