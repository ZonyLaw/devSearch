# Generated by Django 3.2 on 2023-04-22 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20230422_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='createed',
            new_name='created',
        ),
    ]
