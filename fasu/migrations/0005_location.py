# Generated by Django 5.0.6 on 2024-12-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasu', '0004_remove_backgroundimage_bg_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the location', max_length=255)),
                ('address', models.TextField(help_text='Address of the location')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, help_text='Latitude of the location', max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, help_text='Longitude of the location', max_digits=9, null=True)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
    ]