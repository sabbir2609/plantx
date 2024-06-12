# Generated by Django 5.0.6 on 2024-06-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_servicetypefeature_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicetype',
            options={'ordering': ['serial'], 'verbose_name': 'Service Plan', 'verbose_name_plural': 'Service Plans'},
        ),
        migrations.AddField(
            model_name='servicetype',
            name='serial',
            field=models.IntegerField(blank=True, help_text='Enter the serial number for the service type.', null=True),
        ),
    ]
