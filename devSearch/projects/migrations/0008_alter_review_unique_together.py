# Generated by Django 3.2 on 2023-05-21 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230429_1940'),
        ('projects', '0007_auto_20230521_1317'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]