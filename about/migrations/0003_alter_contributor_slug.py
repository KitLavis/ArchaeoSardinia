# Generated by Django 4.2.9 on 2024-01-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_contributor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
