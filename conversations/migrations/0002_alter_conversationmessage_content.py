# Generated by Django 4.0.6 on 2023-04-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='content',
            field=models.TextField(),
        ),
    ]
