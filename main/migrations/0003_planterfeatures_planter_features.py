# Generated by Django 5.0.6 on 2024-06-20 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_plant_tags_alter_plantimage_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanterFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the planter features.', max_length=50)),
            ],
            options={
                'verbose_name': 'Planter Feature',
                'verbose_name_plural': 'Planter Features',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='planter',
            name='features',
            field=models.ManyToManyField(blank=True, help_text='Select the features that describe the planter.', to='main.planterfeatures'),
        ),
    ]
