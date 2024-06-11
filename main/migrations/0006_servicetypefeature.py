# Generated by Django 5.0.6 on 2024-06-11 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_planter_is_custom'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTypeFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of the feature.', max_length=100)),
                ('service_type', models.ForeignKey(help_text='Select the service type for the feature.', on_delete=django.db.models.deletion.CASCADE, to='main.servicetype')),
            ],
            options={
                'verbose_name': 'Service Type Feature',
                'verbose_name_plural': 'Service Type Features',
                'ordering': ['title'],
            },
        ),
    ]
