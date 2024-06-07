# Generated by Django 5.0.6 on 2024-06-06 10:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_plant_options_alter_plantcategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, help_text='Enter the name of the plant.', max_length=100),
            preserve_default=False,
        ),
    ]