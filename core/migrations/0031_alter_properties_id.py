# Generated by Django 4.0.6 on 2023-05-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_remove_properties_uuid_properties_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
