# Generated by Django 5.0.6 on 2024-12-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backgroundimage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bg_image', models.ImageField(upload_to='bg_image')),
            ],
        ),
    ]
