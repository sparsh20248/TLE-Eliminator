# Generated by Django 4.0.1 on 2022-01-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0008_resources_description_resources_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='slides',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
