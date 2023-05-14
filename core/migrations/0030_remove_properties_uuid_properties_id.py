# Generated by Django 4.2 on 2023-05-14 14:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_remove_properties_id_alter_properties_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='uuid',
        ),
        migrations.AddField(
            model_name='properties',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]