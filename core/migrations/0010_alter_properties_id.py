# Generated by Django 4.0.6 on 2023-05-03 11:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_like_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
