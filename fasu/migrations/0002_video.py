# Generated by Django 5.0.6 on 2024-11-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, upload_to='videos/')),
                ('videoname', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_upload', models.DateField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
